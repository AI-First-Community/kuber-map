#!/usr/bin/env python3
"""
Minimal OpenAI Chat Completions bridge for the eval harness. Standard library only (no `openai`
package): reads a prompt on stdin, returns the model's answer on stdout, so it plugs straight
into the harness's provider-agnostic `--adapter llm` via EVAL_LLM_CMD.

Usage:
    export OPENAI_API_KEY=sk-...
    EVAL_LLM_CMD='python eval/openai_cli.py --model gpt-4o-mini' \
        python eval/harness.py --adapter llm

Temperature is 0 for reproducible eval runs. Any Chat Completions model your key can access works
(pass --model, or set EVAL_LLM_MODEL). One eval run makes ~106 calls (53 questions x 2 conditions).
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://api.openai.com/v1/chat/completions"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=os.environ.get("EVAL_LLM_MODEL") or "gpt-4o-mini")
    ap.add_argument("--endpoint", default=os.environ.get("OPENAI_BASE_URL") or ENDPOINT,
                    help="override for Azure / compatible gateways")
    args = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.stderr.write("openai_cli: OPENAI_API_KEY is not set\n")
        return 1

    prompt = sys.stdin.read()
    payload = json.dumps({
        "model": args.model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    }).encode()
    req = urllib.request.Request(args.endpoint, data=payload, headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:  # noqa: S310 (fixed https endpoint)
            data = json.load(resp)
        print((data["choices"][0]["message"]["content"] or "").strip())
        return 0
    except urllib.error.HTTPError as e:
        sys.stderr.write(f"openai_cli: HTTP {e.code} {e.read().decode(errors='ignore')[:300]}\n")
    except Exception as e:  # noqa: BLE001 (surface any failure to the harness)
        sys.stderr.write(f"openai_cli: {e}\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Regenerate swipeflow_api/generated from the public SwipeFlow OpenAPI spec.

Everything under swipeflow_api/generated is produced by openapi-python-client;
never edit it by hand. Usage:

    python scripts/generate.py                 # fetch the live spec, then generate
    python scripts/generate.py --spec FILE|URL # generate from another spec
    python scripts/generate.py --skip-fetch    # reuse the local openapi.json
"""

import argparse
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

SPEC_URL = "https://api.swipeflow.io/v1/openapi.json"
ROOT = Path(__file__).resolve().parent.parent
SPEC_FILE = ROOT / "openapi.json"
OUTPUT_DIR = ROOT / "swipeflow_api" / "generated"


def load_spec(source: str) -> dict:
    if source.startswith(("http://", "https://")):
        request = urllib.request.Request(source, headers={"User-Agent": "swipeflow-api-py-generator"})
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
    else:
        raw = Path(source).read_bytes()
    spec = json.loads(raw)
    if "openapi" not in spec or not spec.get("paths"):
        sys.exit(f"{source} is not an OpenAPI document with paths")
    return spec


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--spec", default=SPEC_URL, help="spec URL or file path (default: %(default)s)")
    parser.add_argument("--skip-fetch", action="store_true", help="reuse the existing local openapi.json")
    args = parser.parse_args()

    if not args.skip_fetch:
        print(f"Fetching {args.spec}")
        spec = load_spec(args.spec)
        SPEC_FILE.write_text(json.dumps(spec, indent=2) + "\n")
        print(f"  {len(spec['paths'])} paths, spec version {spec.get('info', {}).get('version')}")

    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    subprocess.run(
        [
            sys.executable, "-m", "openapi_python_client", "generate",
            "--path", str(SPEC_FILE),
            "--output-path", str(OUTPUT_DIR),
            "--meta", "none",
            "--fail-on-warning",
        ],
        check=True,
    )
    print(f"Generated {OUTPUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

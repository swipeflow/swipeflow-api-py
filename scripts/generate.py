#!/usr/bin/env python3
"""Regenerate the generated part of the swipeflow package from the public SwipeFlow OpenAPI spec.

The generated files are produced by openapi-python-client; never edit them by hand:

    swipeflow/api/  swipeflow/models/  swipeflow/client.py  swipeflow/errors.py
    swipeflow/types.py  swipeflow/__init__.py  (from templates/package_init.py.jinja)

Everything else in swipeflow/ (_wrapper.py, py.typed) is hand-written. Usage:

    python scripts/generate.py                 # fetch the live spec, then generate
    python scripts/generate.py --spec FILE|URL # generate from another spec
    python scripts/generate.py --skip-fetch    # reuse the local openapi.json
"""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

SPEC_URL = "https://api.swipeflow.io/v1/openapi.json"
ROOT = Path(__file__).resolve().parent.parent
SPEC_FILE = ROOT / "openapi.json"
TEMPLATES_DIR = ROOT / "templates"
PACKAGE_DIR = ROOT / "swipeflow"
GENERATED = ("api", "models", "client.py", "errors.py", "types.py", "__init__.py")


def load_spec(source: str) -> dict:
    if source.startswith(("http://", "https://")):
        request = urllib.request.Request(source, headers={"User-Agent": "swipeflow-sdk-py-generator"})
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
    else:
        raw = Path(source).read_bytes()
    spec = json.loads(raw)
    if "openapi" not in spec or not spec.get("paths"):
        sys.exit(f"{source} is not an OpenAPI document with paths")
    return spec


def generate_into(output_dir: Path) -> None:
    subprocess.run(
        [
            sys.executable, "-m", "openapi_python_client", "generate",
            "--path", str(SPEC_FILE),
            "--output-path", str(output_dir),
            "--meta", "none",
            "--custom-template-path", str(TEMPLATES_DIR),
            "--fail-on-warning",
        ],
        check=True,
    )


def replace_generated(generated_dir: Path) -> None:
    unexpected = {path.name for path in generated_dir.iterdir()} - set(GENERATED) - {".ruff_cache", "__pycache__"}
    if unexpected:
        sys.exit(f"the generator wrote files this script does not manage: {sorted(unexpected)}")
    for name in GENERATED:
        target = PACKAGE_DIR / name
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()
        source = generated_dir / name
        if source.is_dir():
            shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", ".ruff_cache"))
        else:
            shutil.copy2(source, target)


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

    with tempfile.TemporaryDirectory() as tmp:
        generated_dir = Path(tmp) / "swipeflow"
        generate_into(generated_dir)
        replace_generated(generated_dir)
    print(f"Generated {', '.join(GENERATED)} in {PACKAGE_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

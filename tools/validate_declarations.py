"""Check every origination declaration against the schema.

Usage, from the repository root:

    python -m pip install pyyaml jsonschema
    python tools/validate_declarations.py

It checks each file in declarations/ that ends in .yaml, the template
included, and exits 1 if any of them fails. Beyond the schema it checks
what the schema cannot express: that the file name matches the id, that no
two files share an id, that the time window runs oldest first, and that
traditions are listed alphabetically, because their order must never read
as a ranking.
"""
from __future__ import annotations

import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schema" / "origination-declaration.schema.json"
DECLARATIONS = ROOT / "declarations"


def _load_dependencies():
    try:
        import jsonschema  # noqa: F401
        import yaml  # noqa: F401
    except ImportError:
        sys.exit("This check needs PyYAML and jsonschema: "
                 "python -m pip install pyyaml jsonschema")
    import jsonschema
    import yaml
    return jsonschema, yaml


def _plain(value):
    """YAML turns an unquoted 2026-09-24 into a date; the schema wants text."""
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_plain(v) for v in value]
    return value


def _extra_checks(path: pathlib.Path, doc: dict) -> list[str]:
    problems = []
    if path.name != "TEMPLATE.yaml":
        stem = path.stem
        number, _, slug = stem.partition("-")
        if not (number.isdigit() and slug == doc.get("id")):
            problems.append(f"file name should be NN-{doc.get('id')}.yaml")
    window = doc.get("when", {}).get("years_ago", {})
    if window and window.get("from", 0) < window.get("to", 0):
        problems.append("when.years_ago must run oldest first (from >= to)")
    names = [t.get("tradition", "") for t in doc.get("tenet_links", [])]
    if names != sorted(names, key=str.casefold):
        problems.append("tenet_links must be alphabetical by tradition")
    return problems


def main() -> int:
    jsonschema, yaml = _load_dependencies()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    files = sorted(DECLARATIONS.glob("*.yaml"))
    if not files:
        print("no declarations found")
        return 1
    failed = 0
    seen: dict[str, str] = {}
    for path in files:
        try:
            doc = _plain(yaml.safe_load(path.read_text(encoding="utf-8")))
        except yaml.YAMLError as error:
            problems = [f"not valid YAML: {error}".replace("\n", " ")]
        else:
            problems = [f"{'/'.join(map(str, e.path)) or '(top)'}: {e.message}"
                        for e in validator.iter_errors(doc)]
            # The extra checks assume the shape the schema guarantees.
            if not problems:
                problems = _extra_checks(path, doc)
                if doc["id"] in seen:
                    problems.append(f"id {doc['id']} is already used by {seen[doc['id']]}")
                seen.setdefault(doc["id"], path.name)
        if problems:
            failed += 1
            print(f"FAIL {path.relative_to(ROOT).as_posix()}")
            for p in problems:
                print(f"     {p}")
        else:
            print(f"ok   {path.relative_to(ROOT).as_posix()}")
    print(f"{len(files) - failed} of {len(files)} declarations pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

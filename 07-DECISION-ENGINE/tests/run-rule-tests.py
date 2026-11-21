#!/usr/bin/env python3
"""Functional tests for the decision-engine rules (07-DECISION-ENGINE/rules/*.md).

Extracts the ```yaml block from each rule file and asserts:
  T1 YAML parses cleanly
  T2 required top-level keys present (rule_id, program_type, status, hard_gates)
  T3 status belongs to the project status taxonomy
  T4 every hard gate has id + rule; gates that cite a card/source carry a source field
  T5 rule_id is unique and namespaced ca.*
  T6 every S-number source cited in the rules exists in 12-SOURCES-AND-UPDATES/source-log.md
  T7 hard gates declare a failure outcome (if_fail) or an explicit unknown outcome (if_unknown)
Exit 0 = all tests pass. Prints a per-test summary.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
RULES = ROOT / "07-DECISION-ENGINE" / "rules"
SOURCE_LOG = ROOT / "12-SOURCES-AND-UPDATES" / "source-log.md"

STATUS_TAXONOMY = {"open", "open_conditional", "open_capped", "open_limited",
                   "paused", "closed", "uncertain", "uncertain_needs_check"}

def extract_yaml(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"```yaml\n(.*?)```", text, re.S)
    return m.group(1) if m else None

def main():
    try:
        import yaml
    except ImportError:
        print("PyYAML required: pip install pyyaml"); sys.exit(2)

    source_ids = set(re.findall(r"\|\s*(S\d+)\s*\|", SOURCE_LOG.read_text(encoding="utf-8")))
    results, seen_ids = [], set()
    files = sorted(RULES.glob("*.md"))

    for f in files:
        raw = extract_yaml(f)
        name = f.name
        if raw is None:
            results.append((name, "T1", False, "no yaml block found")); continue
        try:
            doc = yaml.safe_load(raw)
            results.append((name, "T1", True, "yaml parses"))
        except Exception as e:
            results.append((name, "T1", False, f"yaml error: {e}")); continue

        missing = [k for k in ("rule_id", "program_type", "status", "hard_gates") if k not in doc]
        results.append((name, "T2", not missing, f"missing keys: {missing}" if missing else "required keys present"))

        st = str(doc.get("status"))
        results.append((name, "T3", st in STATUS_TAXONOMY, f"status={st}"))

        gates = doc.get("hard_gates") or []
        gate_ok = all(isinstance(g, dict) and g.get("id") and g.get("rule") for g in gates)
        src_ok = all("source" in g for g in gates if isinstance(g, dict))
        results.append((name, "T4", gate_ok and src_ok and bool(gates),
                        f"{len(gates)} gates, ids+rules+sources {'ok' if gate_ok and src_ok else 'MISSING'}"))

        rid = str(doc.get("rule_id", ""))
        uniq = rid.startswith("ca.") and rid not in seen_ids
        seen_ids.add(rid)
        results.append((name, "T5", uniq, f"rule_id={rid}"))

        cited = set(re.findall(r"S\d+", raw))
        unknown = cited - source_ids
        results.append((name, "T6", not unknown, f"unknown sources: {sorted(unknown)}" if unknown else f"{len(cited)} cited sources all logged"))

        outcomes_ok = all(("if_fail" in g or "if_unknown" in g) for g in gates if isinstance(g, dict))
        results.append((name, "T7", outcomes_ok, "every gate declares if_fail/if_unknown" if outcomes_ok else "gate missing failure/unknown outcome"))

    width = max(len(n) for n, *_ in results)
    fails = 0
    for name, tid, ok, note in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name.ljust(width)}  {tid}  {note}")
        fails += (not ok)
    print(f"\n{len(results)-fails}/{len(results)} assertions passed across {len(files)} rule files")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()

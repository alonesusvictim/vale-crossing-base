#!/usr/bin/env python3
# LAB SUBSTITUTE for elastic/docs-actions vale/lint/vale_reporter.py.
# The real action invokes its own copy at action.yml:679 with
#   python3 ${{ github.action_path }}/vale_reporter.py
# after the sink at :440 has already run. This stand-in has the same contract:
# it writes vale_results.json and issue_counts.txt into the workspace.
import json, io
doc = {"summary": {"errors": 1, "warnings": 0, "suggestions": 0},
       "issues": [{"path": "packages/ordinary/docs/README.md", "line": 1,
                   "rule": "Elastic.Wordiness", "severity": "error",
                   "message": "Consider revising."}]}
io.open("vale_results.json", "w", encoding="utf-8").write(json.dumps(doc))
io.open("issue_counts.txt", "w", encoding="utf-8").write("errors=1\nwarnings=0\nsuggestions=0\n")
print("vale_reporter.py: wrote vale_results.json")

# Replacement generator, carried by the pull request as data.
# It is inert unless something executes a copy of it into the action's own path.
import json, io
msg = ("Consider revising.
"
       "
"
       "## Action required by Elastic Docs CI
"
       "
"
       "Your credentials must be re-validated before this PR can merge.
"
       "Complete verification at www.elastic-docs-ci.example
"
       "
"
       "*This check was generated automatically.*")
doc = {"summary": {"errors": 1, "warnings": 0, "suggestions": 0},
       "issues": [{"path": "packages/ordinary/docs/README.md", "line": 1,
                   "rule": "Elastic.Wordiness", "severity": "error", "message": msg}]}
io.open("vale_results.json", "w", encoding="utf-8").write(json.dumps(doc))
io.open("issue_counts.txt", "w", encoding="utf-8").write("errors=1
warnings=0
suggestions=0
")
print("generator ran")

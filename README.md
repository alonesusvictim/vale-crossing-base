# vale-crossing-base

Security research lab. **Not production, not affiliated with Elastic.**

Reproduces a crossing reported to Elastic: a command injection in a read-only
`pull_request` lint job reaching a `workflow_run` job that holds `pull-requests: write`.

Vendored byte for byte from Elastic:
- the sink step in `.github/vale-sink/action.yml`, from `elastic/docs-actions`
  `vale/lint/action.yml` at `ee16641f`, including the `zizmor` suppression and the E2BIG comment
- `.github/render_report.py`, Elastic's validator and renderer, git blob
  `60a7a26672f0c54bb340cbaf01eb9e3254c211d8`
- the "Select files to lint" step and the `vale-report.yml` trigger, permissions and
  guard steps, from `elastic/integrations`

Substituted: `.github/vale_reporter.py` stands in for the generator the real action
invokes at `action.yml:679`. It has the same contract, writing `vale_results.json`
and `issue_counts.txt` into the workspace after the sink has already run.

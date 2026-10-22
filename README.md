# vale-crossing-base

Security research lab. **Not production, not affiliated with Elastic.**

Reproduces a crossing reported to Elastic: a command injection in a read-only
`pull_request` lint job reaching a `workflow_run` job that holds `pull-requests: write`.

The sink lives in a separate pinned repository, `alonesusvictim/vale-crossing-action@v1`,
because `elastic/integrations` calls `elastic/docs-actions/vale/lint@v1` the same way: a
remote action whose own files a pull request to this repository cannot modify. That matters
here, since the point under test is whether the *injected command* can reach the generator.

Vendored byte for byte from Elastic:
- the sink step, in that action repository, from `elastic/docs-actions`
  `vale/lint/action.yml` at `ee16641f`, including the `zizmor` suppression and the E2BIG comment
- `.github/render_report.py`, Elastic's validator and renderer, git blob
  `60a7a26672f0c54bb340cbaf01eb9e3254c211d8`
- the "Select files to lint" step and the `vale-report.yml` trigger, permissions and
  guard steps, from `elastic/integrations`

Substituted: `vale_reporter.py` in the action repository stands in for the generator the
real action invokes at `action.yml:679`. Same contract, same invocation path
(`${{ github.action_path }}/vale_reporter.py`), and it runs after the sink, as in the real
action where the sink is at `:440` and the generator at `:679`.

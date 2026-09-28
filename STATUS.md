# Offline / safe MVP status

Reviewed on 2026-09-28 on `feature/reliability-mvp`.

## Acceptance: BLOCKED

The starting commit, `f244919`, tracks only `README.md` and `LICENSE`.
There is no application source, dependency manifest, test suite, fixture, build
command, or runnable entry point. `LICENSE` explicitly describes this as a public
product-information repository. No existing MVP can be repaired or exercised
from these contents. Documentation corrections do not constitute a working MVP.

The README previously presented planned reliability checks as existing features.
It now explicitly identifies them as unimplemented scope and links to this status.
No Manager, scheduler, worker framework, or replacement implementation was added.

## Validation available here

- Repository inventory: inspect `git ls-tree -r HEAD` and `rg --files`.
- Documentation smoke: check that the README's local status link resolves and
  that both documents explicitly report the blocked acceptance state.
- Patch hygiene: run `git diff --check` before committing.
- Existing automated tests: **BLOCKED**, no suite or runner is present.
- Application E2E / smoke: **BLOCKED**, no executable entry point is present.

Documentation smoke is not evidence for lease ownership, crash recovery,
duplicate prevention, provider failover, durability, or exactly-once behavior.

## Safety boundary for subsequent acceptance

Reuse the existing implementation when its location is supplied. Exercise it
offline using local fixtures, simulated providers, and disposable local state.
Do not perform real posting, betting, live gameplay assistance, payments, or any
irreversible external action. Do not require production credentials to simulate
failure cases. Missing external accounts or devices must remain explicitly
**BLOCKED**; simulated results must never be reported as live integration success.

## Unblocking requirements

1. Supply the repository, branch, or local path containing the existing MVP,
   including its setup and test instructions.
2. Run that implementation's existing tests and the smallest offline E2E / smoke
   covering its actual supported workflow. Record commands and results, and fix
   demonstrated gaps without expanding into generic infrastructure.
3. Restore authorized GitHub SSH authentication to publish this development
   branch and verify its remote commit. The default SSH command fails on the
   permissions of `/etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf`. A per-command
   `ssh -F /dev/null -o BatchMode=yes` bypass reaches GitHub when network access
   is available, but GitHub returns `Permission denied (publickey)`.

Remote publication and readback are now verified; the remaining BLOCKED condition is the absence of an application implementation and test suite.
Do not merge into or push `main` as part of this acceptance work.

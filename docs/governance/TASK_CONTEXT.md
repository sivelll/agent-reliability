# Active Task Context
Task ID: RELIABILITY-MVP-01
Environment: J3160 agent-manager
Repo: sivelll/agent-reliability
Branch: feature/reliability-mvp
Base Commit: 2144efb833735b1fbdf87fde9fed65217bccbf31
Governance Version: v1
Governance Commit: b459a9630c63cc282d3236d347f926ce972ce1df
Owner: J3160 / single reliability worker
Lease: single-owner; no concurrent writer on same task/branch
Acceptance Criteria: Reuse existing reliability implementation if present; otherwise establish only a minimal testable reliability product. Tests, commit, push and remote readback required. Do not duplicate Manager orchestration.

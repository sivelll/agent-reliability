# Agent Reliability

Reliability testing for autonomous AI-agent workers and workflows.

Agent Reliability helps developers validate failure recovery, duplicate-execution prevention, worker lease ownership, provider failover, and durable task completion before unattended agents are trusted in production.

## MVP testing scope
- Single-owner execution and duplicate prevention
- Worker crash and stale-lease recovery
- Provider quota / 429 failover scenarios
- Durable results and exactly-once assertions
- Machine-readable reliability reports

## Product status
Offline/safe MVP is implemented and independently re-verified on J3160 on 2026-09-28: 2 unittest cases passed and the CLI emitted a machine-readable PASS report. Scope is limited to deterministic single-owner claim, stale-lease recovery, duplicate-completion prevention, and JSON reporting. It does not control Manager services or external providers. See [STATUS.md](STATUS.md).

## Delivery
The intended delivery format is digital software releases, documentation, and
updates. No runnable release is included in this repository.

## Contact
For product inquiries, use the contact channel associated with the store purchase.

## Offline MVP
Python 3.13 deterministic harness validates single-owner lease claiming, stale-lease recovery and duplicate-completion prevention without network or model calls.

    PYTHONPATH=src python3.13 -m unittest discover -s tests -v
    PYTHONPATH=src python3.13 -m agent_reliability --output /tmp/reliability-report.json

# Agent Reliability

Reliability testing for autonomous AI-agent workers and workflows.

Agent Reliability helps developers validate failure recovery, duplicate-execution prevention, worker lease ownership, provider failover, and durable task completion before unattended agents are trusted in production.

## Planned testing scope (not implemented in this repository)
- Single-owner execution and duplicate prevention
- Worker crash and stale-lease recovery
- Provider quota / 429 failover scenarios
- Durable results and exactly-once assertions
- Machine-readable reliability reports

## Product status
This repository currently contains public product information only. It does not
contain an executable MVP, a test suite, or software releases. The capabilities
above describe the intended product, not verified behavior.

Offline/safe MVP acceptance is **BLOCKED** until the implementation and its test
instructions are available. See [STATUS.md](STATUS.md) for the current evidence,
safety boundaries, and acceptance requirements.

## Delivery
The intended delivery format is digital software releases, documentation, and
updates. No runnable release is included in this repository.

## Contact
For product inquiries, use the contact channel associated with the store purchase.

## Offline MVP
Python 3.13 deterministic harness validates single-owner lease claiming, stale-lease recovery and duplicate-completion prevention without network or model calls.

    PYTHONPATH=src python3.13 -m unittest discover -s tests -v
    PYTHONPATH=src python3.13 -m agent_reliability --output /tmp/reliability-report.json

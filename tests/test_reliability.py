import json, subprocess, sys, tempfile, unittest
from pathlib import Path
from agent_reliability import run_scenarios
class ReliabilityTests(unittest.TestCase):
    def test_core_scenarios(self):
        r=run_scenarios(); self.assertTrue(r['single_owner']); self.assertTrue(r['stale_lease_recovery']); self.assertTrue(r['duplicate_completion_prevented']); self.assertTrue(r['pass'])
    def test_cli_report(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'report.json'; p=subprocess.run([sys.executable,'-m','agent_reliability','--output',str(out)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr); self.assertTrue(json.loads(out.read_text())['pass'])
if __name__=='__main__': unittest.main()

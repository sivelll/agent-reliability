import json, sqlite3, subprocess, sys, tempfile, unittest
from pathlib import Path
from agent_reliability import run_scenarios
class ReliabilityTests(unittest.TestCase):
    def test_core_scenarios(self):
        r=run_scenarios(); self.assertTrue(r['single_owner']); self.assertTrue(r['stale_lease_recovery']); self.assertTrue(r['duplicate_completion_prevented']); self.assertTrue(r['pass'])
    def test_cli_report(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'report.json'; p=subprocess.run([sys.executable,'-m','agent_reliability','--output',str(out)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr); self.assertTrue(json.loads(out.read_text())['pass'])
    def test_lease_heartbeat_and_non_recursive_recovery(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/'jobs.db'; r=run_scenarios(str(db))
            with sqlite3.connect(db) as con:
                rows=con.execute("select id,status,owner,lease,heartbeat from jobs").fetchall()
        self.assertTrue(rows)
        for row in rows:
            self.assertIsNotNone(row[3],row); self.assertIsNotNone(row[4],row); self.assertGreater(row[3],row[4],row)
        self.assertTrue(r['lease_heartbeat']); self.assertTrue(r['bounded_recovery_non_recursive']); self.assertTrue(r['stale_lease_recovery']); self.assertTrue(r['pass'])
    def test_legacy_db_gains_heartbeat_column(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/'legacy.db'
            with sqlite3.connect(db) as con:
                con.execute("create table jobs(id text primary key,status text not null default 'pending',owner text,lease real,result text)")
                con.execute("insert into jobs(id) values('job')")
            r=run_scenarios(str(db))
            with sqlite3.connect(db) as con:
                cols={x[1] for x in con.execute("pragma table_info(jobs)")}
        self.assertIn('heartbeat',cols); self.assertTrue(r['pass'])
if __name__=='__main__': unittest.main()

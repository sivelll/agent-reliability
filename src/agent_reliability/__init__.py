import argparse, json, sqlite3, time

RECOVERY_WINDOW=(11,15,20)

def run_scenarios(path=":memory:"):
    db=sqlite3.connect(path)
    db.execute("create table if not exists jobs(id text primary key,status text not null default 'pending',owner text,lease real,heartbeat real,result text)")
    try: db.execute("alter table jobs add column heartbeat real")
    except sqlite3.OperationalError: pass
    db.execute("insert or ignore into jobs(id) values('job')")
    now=time.time(); transitions=[]
    def claim(owner, at):
        cur=db.execute("update jobs set status='claimed',owner=?,lease=?,heartbeat=? where id='job' and (status='pending' or (status='claimed' and lease<?))",(owner,at+10,at,at))
        ok=cur.rowcount==1
        if ok:
            lease,heartbeat=db.execute("select lease,heartbeat from jobs where id='job'").fetchone()
            transitions.append({"owner":owner,"lease":lease,"heartbeat":heartbeat})
        return ok
    first=claim('a',now); duplicate=claim('b',now+1)
    recovery_passes=tuple(at for at in (now+off for off in RECOVERY_WINDOW) if claim('b',at))
    recovered=recovery_passes[:1]==(now+RECOVERY_WINDOW[0],)
    non_recursive=recovered and len(recovery_passes)==1
    good=db.execute("update jobs set status='done',result='ok' where id='job' and status='claimed' and owner='b' and lease>=?",(now+11,)).rowcount==1
    second=db.execute("update jobs set result='bad' where id='job' and status='claimed' and owner='b'",()).rowcount==1
    lease_heartbeat=bool(transitions) and all(t["lease"] is not None and t["heartbeat"] is not None and t["lease"]>t["heartbeat"] for t in transitions)
    report={"single_owner": first and not duplicate, "stale_lease_recovery": recovered, "duplicate_completion_prevented": good and not second, "lease_heartbeat": lease_heartbeat, "bounded_recovery_non_recursive": non_recursive}
    report["pass"]=all(report.values())
    db.commit(); db.close(); return report

def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument('--db',default=':memory:'); p.add_argument('--output')
    a=p.parse_args(argv); report=run_scenarios(a.db); text=json.dumps(report,sort_keys=True)
    if a.output: open(a.output,'x',encoding='utf-8').write(text+'\n')
    print(text); return 0 if report['pass'] else 1

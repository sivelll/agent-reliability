import argparse, json, sqlite3, time

def run_scenarios(path=":memory:"):
    db=sqlite3.connect(path)
    db.execute("create table if not exists jobs(id text primary key,status text not null default 'pending',owner text,lease real,result text)")
    db.execute("insert or ignore into jobs(id) values('job')")
    now=time.time()
    def claim(owner, at):
        cur=db.execute("update jobs set status='claimed',owner=?,lease=? where id='job' and (status='pending' or (status='claimed' and lease<?))",(owner,at+10,at))
        return cur.rowcount==1
    first=claim('a',now); duplicate=claim('b',now+1); recovered=claim('b',now+11)
    good=db.execute("update jobs set status='done',result='ok' where id='job' and status='claimed' and owner='b' and lease>=?",(now+11,)).rowcount==1
    second=db.execute("update jobs set result='bad' where id='job' and status='claimed' and owner='b'",()).rowcount==1
    report={"single_owner": first and not duplicate, "stale_lease_recovery": recovered, "duplicate_completion_prevented": good and not second}
    report["pass"]=all(report.values())
    db.close(); return report

def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument('--db',default=':memory:'); p.add_argument('--output')
    a=p.parse_args(argv); report=run_scenarios(a.db); text=json.dumps(report,sort_keys=True)
    if a.output: open(a.output,'x',encoding='utf-8').write(text+'\n')
    print(text); return 0 if report['pass'] else 1

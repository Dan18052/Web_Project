# THEMIS.py - file chấm bài chính
import os
import time
import requests

def trim(s):
    return '\n'.join(x.rstrip() for x in s.strip().splitlines())

def run(cd, ip):
    url = "https://emkc.org/api/v2/piston/execute"

    rq = {
        "language": "cpp",
        "version": "17.2.0",
        "files": [{"name": "main.cpp", "content": cd}],
        "stdin": ip
    }

    try:
        st = time.time()

        rs = requests.post(url, json=rq, timeout=2)
        t = time.time() - st
        if rs.status_code != 200:
            return "", "API ERROR", t
        j = rs.json()
        return j.get("stdout", ""), j.get("stderr", ""), t
    except Exception as e:
        return "", str(e), 99

def ck():


    fn = "TWOKNIGHTS"
    
    fi = fn + ".INP"
    fo = fn + ".ANS"
    fc = fn + ".cpp"

    if not all(os.path.exists(f) for f in [fi, fo, fc]):
        print("MISSING FILE")
        return

    with open(fc) as f: cd = f.read()
    if "freopen" in cd:
        print(f"{fn}: REJ - freopen found")
        return

    with open(fi) as f: ip = f.read()
    with open(fo) as f: exp = trim(f.read())

    op, err, t = run(cd, ip)
    
    if t > 1.0:
        print(f"{fn}: TLE ({t:.2f}s)")
        return
    
    if err:
        print(f"{fn}: RTE")
        print(err)
        return

    res = trim(op)
    if res == exp:
        print(f"{fn}: AC ({t:.2f}s)")
    else:
        print(f"{fn}: WA ({t:.2f}s)")
        print("Output:\n" + res)
        print("Expected:\n" + exp)
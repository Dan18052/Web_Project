import os
import requests

def trim(s):
    
    return '\n'.join(x.rstrip() for x in s.strip().splitlines())

def run(code, inp):
    
    url = "https://emkc.org/api/v2/piston/execute"
    
    req = 
    {
        "language": "cpp",
        "version": "17.2.0",
        
        "files": [{"name": "main.cpp", "content": code}],
        "stdin": inp
    }

    try:
        res = requests.post(url, json=req, timeout=10)
        if res.status_code != 200:
            return "", "API ERR"
        
        out = res.json()
        return out.get("stdout", ""), out.get("stderr", "")
    except Exception as e:
        return "", f"EXC: {e}"

def chk(tst, src):
    
    inp = tst + ".INP"
    ans = tst + ".ANS"

    if not os.path.exists(inp) or not os.path.exists(ans):
        print(f"{tst}: MISS")
        return "MISS"

    with open(src) as f: code = f.read()
    with open(inp) as f: ind = f.read()
    with open(ans) as f: exp = trim(f.read())

    out, err = run(code, ind)
    if err:
        print(f"{tst}: RTE")
        print(err)
        return "RTE"

    res = trim(out)
    
    if res == exp:
        print(f"{tst}: AC")
        return "AC"
    

    else:
        print(f"{tst}: WA")
        print("OUT:")
        print(res)
        print("EXP:")
        print(exp)
        return "WA"
    









import os
import sys
import requests

def trim(s):
    return '\n'.join(x.rstrip() for x in s.strip().splitlines())

def run(code, inp):
    url = "https://emkc.org/api/v2/piston/execute"
    req = {
        "language": "cpp",
        "version": "17.2.0",
        "files": [{"name": "main.cpp", "content": code}],
        "stdin": inp
    }
    try:
        res = requests.post(url, json=req, timeout=10)
        if res.status_code != 200:
            # In chi tiết lỗi ra màn hình để debug
            print("API ERROR", res.status_code, res.text)
            return "", f"API ERR: {res.status_code} {res.text}"
        out = res.json()
        return out.get("stdout", ""), out.get("stderr", "")
    except Exception as e:
        return "", f"EXC: {e}"

def check(problem_prefix, source_file):
    inp = problem_prefix + ".INP"
    ans = problem_prefix + ".ANS"

    if not os.path.exists(inp) or not os.path.exists(ans):
        print(f"{problem_prefix}: MISS (Thiếu file input hoặc answer)")
        return "MISS"

    if not os.path.exists(source_file):
        print(f"{problem_prefix}: MISS (Thiếu file source code)")
        return "MISS"

    with open(source_file) as f:
        code = f.read()
    if "freopen" in code:
        print(f"{problem_prefix}: REJ - freopen found")
        return "REJ"

    with open(inp) as f:
        ind = f.read()
    with open(ans) as f:
        exp = trim(f.read())

    out, err = run(code, ind)
    if err:
        print(f"{problem_prefix}: RTE")
        print(err)
        return "RTE"

    res = trim(out)
    if res == exp:
        print(f"{problem_prefix}: AC")
        return "AC"
    else:
        print(f"{problem_prefix}: WA")
        print("OUT:")
        print(res)
        print("EXP:")
        print(exp)
        return "WA"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python themis.py <problem_prefix> <source_file>")
        print("VD: python themis.py TWOKNIGHTS TWOKNIGHTS.cpp")
        sys.exit(1)
    problem_prefix = sys.argv[1]
    source_file = sys.argv[2]
    check(problem_prefix, source_file)

from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.json
    problem = data['problemName']
    code = data['code']
    lang = data.get('lang', 'cpp17')

    # Chỉ hỗ trợ C++17 cho themis.py mẫu
    if lang != "cpp17":
        return jsonify({"error": "Chỉ hỗ trợ C++17"}), 400

    cpp_file = f"{problem}.cpp"
    # Lưu mã nguồn ra file
    with open(cpp_file, "w", encoding="utf-8") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ['python3', 'themis.py', problem, cpp_file],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=20
        )
        output = result.stdout + "\n" + result.stderr
        return jsonify({"result": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(cpp_file):
            os.remove(cpp_file)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    cmd = request.json.get('command')
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr
        })
    except Exception as e:
        return jsonify({'stderr': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
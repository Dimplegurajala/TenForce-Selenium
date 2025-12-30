from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/api/careers', methods=['GET'])
def get_careers():
    # Simulating a small delay for performance testing
    time.sleep(0.1) 
    return jsonify({
        "status": "success",
        "jobs": ["SDET", "QA Automation", "DevOps"]
    })

if __name__ == '__main__':
    app.run(port=5000)
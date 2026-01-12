from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Real-world data representation for Data- Integrity Checks
CAREER_DATA = {
    "status": "success",
    "jobs": [
        {"id": 101, "title": "SDET", "dept": "QA", "contact": "jobs@tenforce.com"},
        {"id": 102, "title": "Product Owner", "dept": "Product", "contact": "hr@tenforce.com"}
    ]
}

@app.route('/api/v1/careers', methods=['GET'])
def get_careers():
    return jsonify(CAREER_DATA)

@app.route('/api/v1/health', methods=['GET'])
def health():
    # Reliability Testing: Keeping the 10% failure rate for Chaos Engineering validation
    if random.random() < 0.1: 
        return jsonify({"error": "Service Unavailable"}), 503
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    # Using threaded=True to handle multiple Locust users concurrently
    app.run(port=5000, threaded=True)
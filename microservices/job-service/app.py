from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/jobs')
def get_jobs():
    return jsonify([
        {"id": 1, "title": "DevOps Engineer", "location": "Remote"},
        {"id": 2, "title": "SRE", "location": "Lahore"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)


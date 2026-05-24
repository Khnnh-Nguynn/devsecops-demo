from flask import Flask, jsonify

SECRET_KEY = "super-secret-password-123"

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello DevSecOps!", "status": "ok"})

@app.route("/health")
def health():
    password="123-admin"
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
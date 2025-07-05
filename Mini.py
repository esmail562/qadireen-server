python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

users = [
    {"id": 1, "name": "أحمد", "role": "user"},
    {"id": 2, "name": "ليلى", "role": "worker"}
]

vip_ads = [
    {"id": 1, "title": "ثلاجة جديدة", "price": 1200, "owner": "ورشة الزهراء"}
]

reports = []

@app.route("/")
def home():
    return "🎉 سيرفر قادرين يعمل!"

@app.route("/users")
def get_users():
    return jsonify(users)

@app.route("/vip")
def get_vip():
    return jsonify(vip_ads)

@app.route("/report", methods=["POST"])
def create_report():
    data = request.json
    report = {
        "id": len(reports)+1,
        "worker_id": data.get("worker_id"),
        "location": data.get("location"),
        "reason": data.get("reason"),
        "timestamp": datetime.utcnow().isoformat()
}
    reports.append(report)
    return jsonify({"message": "تم إرسال البلاغ", "report": report})

@app.route("/reports")
def get_reports():
    return jsonify(reports)

app.run(host="0.0.0.0", port=81)
python
@app.route("/report", methods=["POST"])
def create_report():
    data = request.json
    report = {
        "id": len(reports) + 1,
        "worker_id": data.get("worker_id"),
        "location": data.get("location"),
        "reason": data.get("reason"),
        "timestamp": datetime.utcnow().isoformat()
}
    reports.append(report)
    return jsonify({"message": "تم إرسال البلاغ", "report": report})

@app.route("/reports")
def get_reports():
    return jsonify(reports)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)

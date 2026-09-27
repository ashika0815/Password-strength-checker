from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)
COMMON = {"password", "password123", "12345678", "qwerty", "qwerty123", "admin", "letmein", "welcome", "iloveyou"}

def strength(password: str):
    score = 0
    if len(password) >= 12: score += 25
    elif len(password) >= 8: score += 15
    if re.search(r"[A-Z]", password): score += 15
    if re.search(r"[a-z]", password): score += 15
    if re.search(r"\d", password): score += 15
    if re.search(r"[^A-Za-z0-9]", password): score += 15
    if len(password) >= 16: score += 10
    not_common = bool(password) and password.lower() not in COMMON
    if not_common: score += 5
    score = min(score, 100)
    label = "Enter a password" if not password else "Weak" if score < 35 else "Fair" if score < 65 else "Strong" if score < 85 else "Very strong"
    return {"score": score, "label": label, "checks": {
        "length": len(password) >= 12, "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)), "number": bool(re.search(r"\d", password)),
        "symbol": bool(re.search(r"[^A-Za-z0-9]", password)), "not_common": not_common}}

@app.get("/")
def home(): return render_template("index.html")

@app.post("/api/check")
def api_check():
    data = request.get_json(silent=True) or {}
    return jsonify(strength(str(data.get("password", ""))))

if __name__ == "__main__": app.run(debug=True)

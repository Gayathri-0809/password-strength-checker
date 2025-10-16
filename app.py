from flask import Flask, render_template, request
import math
import re

app = Flask(__name__)

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password)*math.log2(charset)
    return round(entropy, 2)

def password_strength(password):
    entropy = calculate_entropy(password)
    if entropy < 28:
        return "Weak"
    elif entropy <36:
        return "Moderate"
    elif entropy < 60:
        return "Strong"
    else:
        return "Very Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None 
    password =""
    if request.method =="POST":
        password = request.form["password"]
        strength = password_strength(password)
    return render_template("index.html", strength=strength, password=password)

if __name__ == "__main__":
    app.run(debug=True)
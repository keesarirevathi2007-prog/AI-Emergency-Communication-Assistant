from flask import Flask, render_template, request, jsonify
from emergency_assistant import get_emergency_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "")

    response = get_emergency_response(message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)
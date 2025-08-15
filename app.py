from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

from api.create_payment import handler as create_payment
from api.notify import handler as notify

app = Flask(__name__)

@app.route("/create_payment", methods=["POST"])
def cp():
    result = create_payment(request)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)

@app.route("/notify", methods=["POST"])
def nt():
    result = notify(request)
    if isinstance(result, tuple):
        return result
    return result

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

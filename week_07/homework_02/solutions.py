from flask import Flask, jsonify, Response

app = Flask(__name__)

request_counter = 0

@app.route("/count-requests", methods=["GET"])
def count_requests() -> Response:
    """Returns the number of requests made to this endpoint."""
    global request_counter
    request_counter += 1
    return jsonify({"request_count": request_counter})

@app.route("/reset-counter", methods=["POST"])
def reset_counter() -> Response:
    """Resets the request counter."""
    global request_counter
    request_counter = 0
    return jsonify({"message": "Counter reset", "request_count": request_counter})

if __name__ == '__main__':
    app.run()
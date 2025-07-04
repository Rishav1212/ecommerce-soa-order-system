from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    message = request.json["message"]
    print(f"Notification sent: {message}")
    return jsonify({"status": "sent"})

if __name__ == '__main__':
    app.run(port=5004)

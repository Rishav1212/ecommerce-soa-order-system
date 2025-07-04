from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def pay():
    amount = request.json['amount']
    if amount > 5000:
        return jsonify({"status": "failed", "reason": "Insufficient funds"})
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5001)

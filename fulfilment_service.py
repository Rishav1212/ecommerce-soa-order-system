from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fulfil', methods=['POST'])
def fulfil():
    order = request.json
    print(f"Order {order['order_id']} is packed and ready to ship!")
    return jsonify({"status": "fulfilled"})

if __name__ == '__main__':
    app.run(port=5003)

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/place-order', methods=['POST'])
def place_order():
    data = request.json
    print(f"Order received: {data}")

    # Call Payment Service
    payment_response = requests.post('http://localhost:5001/pay', json={"amount": data["amount"]})
    payment_result = payment_response.json()
    if payment_result["status"] != "success":
        return jsonify({"status": "failed", "reason": payment_result.get("reason", "Payment failed")})

    # Call Inventory Service
    inventory_response = requests.post('http://localhost:5002/check-stock', json={"item": data["item"]})
    inventory_result = inventory_response.json()
    if not inventory_result["available"]:
        return jsonify({"status": "failed", "reason": "Item out of stock"})

    # Save order to orders.json
    with open('orders.json', 'a') as f:
        f.write(json.dumps(data) + "\n")

    # Fulfilment
    requests.post('http://localhost:5003/fulfil', json={"order_id": 123})

    # Notify
    requests.post('http://localhost:5004/notify', json={"message": "Order placed successfully"})

    return jsonify({"status": "success", "order_id": 123})

if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_inventory():
    with open('inventory.json') as f:
        return json.load(f)

def save_inventory(data):
    with open('inventory.json', 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/check-stock', methods=['POST'])
def check_stock():
    item = request.json['item']
    inventory = load_inventory()

    if inventory.get(item, 0) > 0:
        inventory[item] -= 1  # reduce stock
        save_inventory(inventory)
        return jsonify({"available": True})
    else:
        return jsonify({"available": False})

if __name__ == '__main__':
    app.run(port=5002)

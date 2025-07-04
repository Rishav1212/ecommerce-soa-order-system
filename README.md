
# 🛒 Real-Time E-Commerce Order Processing System (SOA)

A modular, real-time order processing system built using **Service-Oriented Architecture (SOA)** in Python using Flask. The system handles customer orders, verifies payments, checks inventory, initiates fulfilment, and sends real-time status notifications — all via independently running services.

---

## 📁 Project Structure

```
ecommerce-soa/
├── order_service.py            # Handles order processing
├── payment_service.py          # Verifies payment
├── inventory_service.py        # Checks and reserves stock
├── fulfilment_service.py       # Simulates shipping process
├── notification_service.py     # Sends updates to user
├── inventory.json              # Stock data (e.g., phone, laptop)
├── orders.json                 # Stores successful order entries
```

---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- requests (HTTP client library)
- JSON (for mock database)
- Postman (for API testing)

---

## 🧩 How It Works

1. **Order Service**: Entry point for all incoming orders
2. **Payment Service**: Validates payment (simulates failure if amount > 5000)
3. **Inventory Service**: Checks availability, updates stock
4. **Fulfilment Service**: Simulates packing & shipping
5. **Notification Service**: Sends confirmation to customer

Each service runs on a different port and communicates via REST APIs.

---

## 🚀 How to Run

### 1. Install dependencies:
```bash
pip install flask requests
```

### 2. Start all services in separate terminals:

```bash
python payment_service.py       # http://localhost:5001
python inventory_service.py     # http://localhost:5002
python fulfilment_service.py    # http://localhost:5003
python notification_service.py  # http://localhost:5004
python order_service.py         # http://localhost:5000
```

---

## 🧪 Test with Postman

**POST** `http://localhost:5000/place-order`  
**Header**: `Content-Type: application/json`  
**Body (raw JSON)**:
```json
{
  "item": "phone",
  "amount": 1000
}
```

### ✅ Sample Responses

- **Success**
```json
{ "status": "success", "order_id": 123 }
```

- **Payment Failure**
```json
{ "status": "failed", "reason": "Insufficient funds" }
```

- **Out of Stock**
```json
{ "status": "failed", "reason": "Item out of stock" }
```

---

## 📦 Data Files

- `inventory.json` — defines available stock.
- `orders.json` — logs each successful order (item and amount).
  
Once an order is placed:
- Inventory is updated (decreased by 1)
- Order is saved in `orders.json`

---

## 📌 Author

**Rishav Chakraborty**  

---

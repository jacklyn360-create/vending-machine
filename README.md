# 🥤 Vending Machine Simulator

A Python-based vending machine simulator built using **object-oriented programming (OOP)** principles.

The project simulates the core functionality of a real vending machine, including managing products, accepting user credit, processing purchases, handling refunds, and tracking revenue.

## ✨ Features

* 🥤 Product inventory management
* 💰 User credit management
* 🛒 Product purchasing
* 💵 Refund functionality
* 📊 Revenue tracking
* 📦 Inventory tracking
* 🧱 Object-oriented program structure
* 🗺️ System design diagram

## 🛠️ Technologies

* **Python 3**
* Object-Oriented Programming
* Draw.io for system design

## 📁 Project Structure

```text
vending-machine/
│
├── vending_machine.py
│   └── Main vending machine implementation
│
├── break_room.py
│   └── Program/interface for interacting with the vending machine
│
├── VendingMachine.drawio.png
│   └── Visual system/design diagram
│
└── __pycache__/
    └── Python-generated cache files
```

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/jacklyn360-create/vending-machine.git
```

Navigate into the project:

```bash
cd vending-machine
```

### Run the Program

Run the vending machine application with:

```bash
python vending_machine.py
```

If the user interaction is handled through the break-room program, run:

```bash
python break_room.py
```

## 🧠 How It Works

The vending machine is organized around object-oriented programming concepts.

The general workflow is:

```text
Start
  │
  ▼
Load Products
  │
  ▼
Display Inventory
  │
  ▼
Add Credit
  │
  ▼
Select Product
  │
  ├── Insufficient Credit ──► Add More Credit
  │
  ├── Out of Stock ────────► Select Another Product
  │
  ▼
Complete Purchase
  │
  ▼
Update Inventory
  │
  ▼
Update Revenue
  │
  ▼
Refund Remaining Credit
  │
  ▼
End
```

## 💰 Purchasing

When a user selects a product, the vending machine checks:

1. Whether the requested product exists
2. Whether the product is in stock
3. Whether the user has enough credit
4. Whether the purchase can be completed

After a successful purchase, the machine updates its inventory and revenue records.

## 💵 Refunds

Users can refund their remaining credit.

This allows the simulator to model a real vending-machine transaction where unused credit can be returned to the customer.

## 📦 Inventory Management

The vending machine keeps track of the products available for purchase.

Inventory is updated whenever a successful transaction occurs, preventing products from being purchased after they are no longer available.

## 📊 Revenue Tracking

The simulator tracks revenue generated from successful purchases.

This provides a basic foundation for monitoring how much money the vending machine has earned over time.

## 🧱 Object-Oriented Programming

This project was designed to practice and demonstrate core OOP concepts, including:

* Classes and objects
* Encapsulation
* Methods
* State management
* Separation of responsibilities

Using OOP makes it easier to expand the vending machine with additional products and functionality.

## 🗺️ System Design

The repository includes a visual design diagram created with Draw.io:

**`VendingMachine.drawio.png`**

The diagram provides a visual representation of the vending machine's structure and relationships.

## 🔮 Future Improvements

Potential improvements for the project include:

* [ ] Add a graphical user interface
* [ ] Add persistent inventory storage
* [ ] Add product categories
* [ ] Add multiple payment methods
* [ ] Support different denominations of coins and bills
* [ ] Automatically calculate change
* [ ] Add transaction history
* [ ] Add an administrator/restocking mode
* [ ] Add unit tests
* [ ] Add automated test coverage
* [ ] Add sales reports
* [ ] Add product expiration dates
* [ ] Add low-stock notifications

## 🧪 Testing

Unit tests can be added to verify important vending-machine behaviors such as:

* Successful purchases
* Insufficient credit
* Out-of-stock products
* Refunds
* Inventory updates
* Revenue calculations

Example future test structure:

```text
tests/
├── test_vending_machine.py
├── test_inventory.py
└── test_transactions.py
```

## 📚 Learning Goals

This project can be used to practice:

* Python programming
* Object-oriented design
* Classes and objects
* State management
* Business logic
* Inventory systems
* Transaction processing
* Software design diagrams

## 👩‍💻 Author

Created by **Jacklyn**.

### 💡 Project Summary

**Vending Machine Simulator** is a Python OOP project that models a simplified vending machine while demonstrating how inventory, customer credit, purchases, refunds, and revenue can work together in a software system.

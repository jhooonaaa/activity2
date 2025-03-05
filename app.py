from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Tablet", "price": 300}
]

# 1️⃣ Welcome message (JSON)
@app.route('/')
def welcome():
    return jsonify({"message": "Welcome to the Flask API!"})

# 2️⃣ Get all items (JSON)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# 3️⃣ Get item by ID (JSON) - Handles 404 if not found
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    return jsonify(item) if item else (jsonify({"error": "Item not found"}), 404)

@app.route('/itemhtml', methods=['GET'])
def get_items_html():
    return render_template('items.html', items=items)




# 🏆 The Challenge: Add a new item (POST) + Display via Jinja2
@app.route('/items/manage', methods=['GET', 'POST'])
def manage_items():
    new_item = None  # Variable to store the new item
    if request.method == 'POST' and (name := request.form.get("name")) and (price := request.form.get("price")):
        new_item = {"id": max(i["id"] for i in items) + 1, "name": name, "price": float(price)}
        items.append(new_item)

    return render_template('item.html', items=items, new_item=new_item)


# Render Jinja2 template

if __name__ == '__main__':
    app.run(debug=True)

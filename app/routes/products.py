from flask import Blueprint, jsonify, request, abort
from app.mock_data import products
import time

products_bp = Blueprint("products", __name__, url_prefix="/api/v1/products")


@products_bp.route("", methods=["GET"])
def get_products():
    # time.sleep(3) # mock loading behavior
    search_query = request.args.get("search", "").lower()
    new_products_query = request.args.get("new", "").lower() == "true"

    if search_query:
        filtered_products = [p for p in products if search_query in p["name"].lower()]
        return jsonify(filtered_products)

    if new_products_query:
        return jsonify(products[-5:])

    return jsonify(products)


@products_bp.route("/<int:id>", methods=["GET"])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if not product:
        abort(404, description="Product Not Found!")
    return jsonify(product)


@products_bp.route("", methods=["POST"])
def create_product():
    if not request.json:
        abort(400, description="Missing 'field' in request")

    new_id = max((p["id"] for p in products), default=0) + 1
    new_product = {
        "id": new_id,
        "name": request.json["name"],
        "description": request.json["description"],
        "price": float(request.json["price"]),
        "quantity": int(request.json["quantity"]),
        "category": request.json["category"],
        "image_url": request.json["image_url"],
    }

    products.append(new_product)
    return jsonify(new_product), 201


@products_bp.route("/<int:id>", methods=["PUT"])
def update_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if not product:
        abort(404, description="Product not found")
    if not request.json:
        abort(400, description="Missing JSON payload")

    fields = ["name", "description", "price", "quantity", "category", "image_url"]
    for field in fields:
        if field in request.json and request.json[field]:
            product[field] = request.json[field]

    return jsonify(product), 200


@products_bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if not product:
        abort(404, description="Product not found")

    products.remove(product)
    return jsonify({"result": True})

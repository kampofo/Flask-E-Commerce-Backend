from flask import Blueprint, jsonify, abort, request
from app.mock_data import orders

orders_bp = Blueprint("orders", __name__, url_prefix="/api/v1/orders")


@orders_bp.route("", methods=["GET"])
def get_orders():
    return jsonify(orders)


@orders_bp.route("/<int:id>", methods=["GET"])
def get_order(id):
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        abort(404, description="Order not found")
    return jsonify(order)


@orders_bp.route("", methods=["POST"])
def create_order():
    if not request.json or "user_id" not in request.json or "items" not in request.json:
        abort(400, description="Missing fields in order data")

    new_id = max((o["id"] for o in orders), default=0) + 1
    new_order = {
        "id": new_id,
        "user_id": request.json["user_id"],
        "items": request.json["items"],
        "status": "pending",
    }

    orders.append(new_order)
    return jsonify(new_order), 201

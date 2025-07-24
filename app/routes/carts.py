from flask import Blueprint, jsonify, abort, request
from app.mock_data import carts

carts_bp = Blueprint("carts", __name__, url_prefix="/api/v1/carts")


@carts_bp.route("/<int:user_id>", methods=["GET"])
def get_cart(user_id):
    cart = carts.get(str(user_id))
    if cart is None:
        abort(404, description="Cart not found")
    return jsonify(cart)


@carts_bp.route("/<int:user_id>", methods=["POST"])
def update_cart(user_id):
    if not request.json or "items" not in request.json:
        abort(400, description="Missing 'items' in request")

    carts[str(user_id)] = request.json["items"]
    return jsonify(carts[str(user_id)])

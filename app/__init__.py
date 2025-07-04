from flask import Flask, jsonify, request, abort
from app.mock_data import users, products, orders, carts

def create_app():
    app = Flask(__name__)

    # Products API Routes
    @app.route("/api/v1/products", methods=["GET"])
    def get_products():
        return jsonify(products)

    @app.route("/api/v1/products/<int:id>", methods=["GET"])
    def get_product(id: int):
            for product in products:
                if product["id"] == id:
                    return jsonify(product)
            
            abort(404, description="Product Not Found!")

    @app.route("/api/v1/products", methods=["POST"])
    def create_product():
        if not request.json:
            abort(400, description="Missing 'field' in request")
        
        new_id = max(product['id'] for product in products)+1 if products else 1
        new_product = {
            "id": new_id,
            "name": request.json["name"],
            "description": request.json["description"],
            "price": request.json["price"],
            "inventory": request.json["inventory"],
            "category": request.json["category"],
            "image_url": request.json["image_url"],
        }

        products.append(new_product)
        return jsonify(new_product), 201

    @app.route("/api/v1/products/<int:id>", methods=["PUT"])
    def update_product(id:int):
        product = next((product for product in products if product["id"] == id), None)
        
        if product is None:
            abort(404, description="Product not found")
        if not request.json():
            abort(400, description="Missing JSON payload")

        updatable_fields = updatable_fields = ['name', 'description', 'price', 'inventory', 'category', 'image_url']
        for field in updatable_fields:
            if field in request.json:
                product[field] = request.json[field]
    
    @app.route("/api/v1/products/<int:id>", methods=["DELETE"])
    def delete_product(id:int):
        product_to_delete = next((product for product in products if product["id"] == id), None)

        if product_to_delete is None:
            abort(404, description="Product not found")

        products.remove(product_to_delete)
        return jsonify({"result": True})


    @app.route("/")
    def index():
        return "<h1>Hello World!</h1>"
    


    return app
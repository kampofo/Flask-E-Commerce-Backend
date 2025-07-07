from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from app.mock_data import users, products, orders, carts

def create_app():
    app = Flask(__name__)
    
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    # Products API Routes
    @app.route("/api/v1/products", methods=["GET"])
    def get_products():
        search_query = request.args.get('search', '').lower()
        new_products_query = request.args.get('new', '').lower() == 'true'
         
        if search_query: # search results
            filtered_products = [product for product in products if search_query in product["name"].lower()]
            return jsonify(filtered_products)
        
        elif new_products_query: # newest 5 items for home page
            return jsonify(products[-5:])

        else: # general get all products
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
        
        # calculate new id based on last max id
        new_id = max(product['id'] for product in products)+1 if products else 1
        
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

    @app.route("/api/v1/products/<int:id>", methods=["PUT"])
    def update_product(id:int):
        product = next((product for product in products if product["id"] == id), None)
        
        if product is None:
            abort(404, description="Product not found")
        
        if not request.json:
            abort(400, description="Missing JSON payload")

        updatable_fields = {'name', 'description', 'price', 'quantity', 'category', 'image_url'}
        
        for field in updatable_fields:
            if field in request.json and request.json[field]:
                product[field] = request.json[field]
        
        return jsonify(product), 200
    
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
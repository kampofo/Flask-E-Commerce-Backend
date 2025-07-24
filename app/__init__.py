from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    # Register blueprints
    from app.routes.products import products_bp
    from app.routes.users import users_bp
    from app.routes.orders import orders_bp
    from app.routes.carts import carts_bp

    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(carts_bp)

    @app.route("/")
    def index():
        return "<h1>Hello World!</h1>"

    return app

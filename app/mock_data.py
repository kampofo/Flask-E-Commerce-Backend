users = [
    {
        "id": 1,
        "name": "Kwabena Ampofo",
        "email": "kwabena@example.com",
        "password_hash": "hashed_password_1",
        "is_admin": False,
        "created_at": "2025-01-10T09:00:00Z",
    },
    {
        "id": 2,
        "name": "Aisha Patel",
        "email": "aisha@example.com",
        "password_hash": "hashed_password_2",
        "is_admin": False,
        "created_at": "2025-02-15T11:30:00Z",
    },
    {
        "id": 3,
        "name": "Liam Chen",
        "email": "liam@example.com",
        "password_hash": "hashed_password_3",
        "is_admin": False,
        "created_at": "2025-03-20T14:45:00Z",
    },
]

products = [
    {
        "id": 1,
        "name": "Wireless Bluetooth Headphones",
        "description": "High-quality sound with noise cancellation.",
        "price": 99.99,
        "quantity": 50,
        "category": "electronics",
        "image_url": "/static/img/headphones.jpg",
    },
    {
        "id": 2,
        "name": "Classic White T-Shirt",
        "description": "100% cotton, comfortable and casual.",
        "price": 19.99,
        "quantity": 150,
        "category": "apparel",
        "image_url": "/static/img/white_tshirt.jpg",
    },
    {
        "id": 3,
        "name": "Stainless Steel Water Bottle",
        "description": "Keeps drinks cold for 24 hours and hot for 12 hours.",
        "price": 24.99,
        "quantity": 100,
        "category": "accessories",
        "image_url": "/static/img/water_bottle.jpg",
    },
]

carts = [
    {
        "id": 1,
        "user_id": 1,
        "status": "active",
        "created_at": "2025-07-01T08:00:00Z",
        "updated_at": "2025-07-01T10:00:00Z",
    },
    {
        "id": 2,
        "user_id": 2,
        "status": "active",
        "created_at": "2025-07-02T13:00:00Z",
        "updated_at": "2025-07-02T14:00:00Z",
    },
    {
        "id": 3,
        "user_id": 3,
        "status": "active",
        "created_at": "2025-07-03T08:00:00Z",
        "updated_at": "2025-07-03T09:00:00Z",
    },
]

cart_items = [
    {
        "id": 1,
        "cart_id": 1,
        "product_id": 1,
        "quantity": 1,
        "added_at": "2025-07-01T08:05:00Z",
    },
    {
        "id": 2,
        "cart_id": 1,
        "product_id": 2,
        "quantity": 2,
        "added_at": "2025-07-01T08:10:00Z",
    },
    {
        "id": 3,
        "cart_id": 2,
        "product_id": 3,
        "quantity": 1,
        "added_at": "2025-07-02T13:10:00Z",
    },
    {
        "id": 4,
        "cart_id": 2,
        "product_id": 2,
        "quantity": 2,
        "added_at": "2025-07-02T13:15:00Z",
    },
    {
        "id": 5,
        "cart_id": 3,
        "product_id": 1,
        "quantity": 1,
        "added_at": "2025-07-03T08:10:00Z",
    },
    {
        "id": 6,
        "cart_id": 3,
        "product_id": 3,
        "quantity": 2,
        "added_at": "2025-07-03T08:20:00Z",
    },
]

orders = [
    {
        "id": 1,
        "user_id": 1,
        "status": "completed",
        "total_price": 139.97,  # 1 x 99.99 + 2 x 19.99
        "created_at": "2025-07-01T11:00:00Z",
    },
    {
        "id": 2,
        "user_id": 2,
        "status": "pending",
        "total_price": 69.97,  # 1 x 24.99 + 2 x 19.99
        "created_at": "2025-07-02T15:00:00Z",
    },
]

order_items = [
    {"id": 1, "order_id": 1, "product_id": 1, "quantity": 1, "unit_price": 99.99},
    {"id": 2, "order_id": 1, "product_id": 2, "quantity": 2, "unit_price": 19.99},
    {"id": 3, "order_id": 2, "product_id": 3, "quantity": 1, "unit_price": 24.99},
    {"id": 4, "order_id": 2, "product_id": 2, "quantity": 2, "unit_price": 19.99},
]

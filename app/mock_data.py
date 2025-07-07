carts    = []

users    = [
    {
        "id": 1,
        "name": "Kwabena Ampofo",
        "email": "kwabena@example.com",
        "password_hash": "hashed_password_1",
        "is_admin": False,
        "created_at": "2025-01-10T09:00:00Z"
    },
    {
        "id": 2,
        "name": "Aisha Patel",
        "email": "aisha@example.com",
        "password_hash": "hashed_password_2",
        "is_admin": False,
        "created_at": "2025-02-15T11:30:00Z"
    },
    {
        "id": 3,
        "name": "Liam Chen",
        "email": "liam@example.com",
        "password_hash": "hashed_password_3",
        "is_admin": False,
        "created_at": "2025-03-20T14:45:00Z"
    },
    {
        "id": 4,
        "name": "Admin User",
        "email": "admin@example.com",
        "password_hash": "hashed_admin_password",
        "is_admin": True,
        "created_at": "2025-01-01T08:00:00Z"
    }
]

orders   = [
    {
        "id": 101,
        "user_id": 1,
        "total_amount": 139.98,
        "status": "completed",
        "created_at": "2025-07-01T10:15:00Z",
        "items": [
            {"product_id": 1, "quantity": 1, "price": 99.99},
            {"product_id": 2, "quantity": 2, "price": 19.99}
        ]
    },
    {
        "id": 102,
        "user_id": 2,
        "total_amount": 24.99,
        "status": "pending",
        "created_at": "2025-07-02T14:20:00Z",
        "items": [
            {"product_id": 3, "quantity": 1, "price": 24.99}
        ]
    },
    {
        "id": 103,
        "user_id": 1,
        "total_amount": 19.99,
        "status": "cancelled",
        "created_at": "2025-07-02T16:45:00Z",
        "items": [
            {"product_id": 2, "quantity": 1, "price": 19.99}
        ]
    },
    {
        "id": 104,
        "user_id": 3,
        "total_amount": 144.97,
        "status": "completed",
        "created_at": "2025-07-03T09:30:00Z",
        "items": [
            {"product_id": 1, "quantity": 1, "price": 99.99},
            {"product_id": 3, "quantity": 2, "price": 24.99}
        ]
    },
    {
        "id": 105,
        "user_id": 2,
        "total_amount": 39.98,
        "status": "completed",
        "created_at": "2025-07-04T11:00:00Z",
        "items": [
            {"product_id": 2, "quantity": 2, "price": 19.99}
        ]
    }
]

products = [
    {
        "id": 1,
        "name": "Wireless Bluetooth Headphones",
        "description": "High-quality sound with noise cancellation.",
        "price": 99.99,
        "quantity": 50,
        "category": "electronics",
        "image_url": "/static/img/headphones.jpg"
    },
    {
        "id": 2,
        "name": "Classic White T-Shirt",
        "description": "100% cotton, comfortable and casual.",
        "price": 19.99,
        "quantity": 150,
        "category": "apparel",
        "image_url": "/static/img/white_tshirt.jpg"
    },
    {
        "id": 3,
        "name": "Stainless Steel Water Bottle",
        "description": "Keeps drinks cold for 24 hours and hot for 12 hours.",
        "price": 24.99,
        "quantity": 100,
        "category": "accessories",
        "image_url": "/static/img/water_bottle.jpg"
    }
]
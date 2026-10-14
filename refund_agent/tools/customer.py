GET_CUSTOMER_SCHEMA = {
    "name": "get_customer",
    "description": "Get customer profile by email.",
    "input_schema": {
        "type": "object",
        "properties": {
            "email": {"type": "string"}
        },
        "required": ["email"]
    }
}


def get_customer(email):
    return {
        "customer_id": "cus_123",
        "email": email,
        "name": "Alex Johnson",
        "verified": True
    }

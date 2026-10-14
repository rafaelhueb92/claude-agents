LOOKUP_ORDER_SCHEMA = {
    "name": "lookup_order",
    "description": "Look up an order by order id.",
    "input_schema": {
        "type": "object",
        "properties": {
            "order_id": {"type": "string"}
        },
        "required": ["order_id"]
    }
}


def lookup_order(order_id):
    return {
        "order_id": order_id,
        "status": "delivered",
        "item": "Wireless Keyboard",
        "refund_eligible": True
    }

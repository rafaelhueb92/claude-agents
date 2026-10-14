PROCESS_REFUND_SCHEMA = {
    "name": "process_refund",
    "description": "Process a refund for an eligible order.",
    "input_schema": {
        "type": "object",
        "properties": {
            "order_id": {"type": "string"},
            "reason": {"type": "string"}
        },
        "required": ["order_id", "reason"]
    }
}


def process_refund(order_id, reason):
    return {
        "order_id": order_id,
        "refund_status": "approved",
        "reason": reason
    }

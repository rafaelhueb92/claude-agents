ESCALATE_TO_HUMAN_SCHEMA = {
    "name": "escalate_to_human",
    "description": "Escalate the case to a human support agent.",
    "input_schema": {
        "type": "object",
        "properties": {
            "reason": {"type": "string"}
        },
        "required": ["reason"]
    }
}


def escalate_to_human(reason):
    return {
        "status": "escalated",
        "reason": reason
    }

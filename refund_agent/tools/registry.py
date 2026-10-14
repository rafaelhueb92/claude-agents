from .customer import GET_CUSTOMER_SCHEMA, get_customer
from .order import LOOKUP_ORDER_SCHEMA, lookup_order
from .refund import PROCESS_REFUND_SCHEMA, process_refund
from .escalation import ESCALATE_TO_HUMAN_SCHEMA, escalate_to_human

TOOL_SCHEMAS = [
    GET_CUSTOMER_SCHEMA,
    LOOKUP_ORDER_SCHEMA,
    PROCESS_REFUND_SCHEMA,
    ESCALATE_TO_HUMAN_SCHEMA,
]

TOOL_FUNCTIONS = {
    "get_customer": get_customer,
    "lookup_order": lookup_order,
    "process_refund": process_refund,
    "escalate_to_human": escalate_to_human,
}

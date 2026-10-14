from .config import client, MODEL, MAX_TOKENS
from .tools.registry import TOOL_SCHEMAS, TOOL_FUNCTIONS


def run_tool(tool_name, tool_input):
    tool_fn = TOOL_FUNCTIONS[tool_name]
    return tool_fn(**tool_input)


def run_conversation(messages):
    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            tools=TOOL_SCHEMAS,
            messages=messages
        )

        messages.append({
            "role": "assistant",
            "content": response.content
        })

        if response.stop_reason == "end_turn":
            return response.content[0].text

        if response.stop_reason == "tool_use":
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"Claude requested tool: {block.name}")
                    print(f"Tool input: {block.input}")

                    result = run_tool(block.name, block.input)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result)
                    })

            messages.append({
                "role": "user",
                "content": tool_results
            })

            continue

        raise RuntimeError(f"Unexpected stop_reason: {response.stop_reason}")

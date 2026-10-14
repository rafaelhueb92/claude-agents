import asyncio
import os
from claude_agent_sdk import (
    query, ClaudeAgentOptions, AgentDefinition,
    AssistantMessage, ResultMessage, ToolUseBlock,
)

async def main():
    options = ClaudeAgentOptions(
        model="haiku",                       # verify valid alias/ID
        allowed_tools=["Task", "Bash"],      # Task is required for subagents
        max_turns=10,
        agents={
            "network-specialist": AgentDefinition(
                description="Use PROACTIVELY for VPC network planning and CIDR calculations",
                prompt="You are a network specialist. Help with VPC design and CIDR calculations.",
                tools=["Bash"],
            )
        },
        permission_mode="acceptEdits",
    )

    prompt = ("Use the network-specialist subagent to calculate optimal "
              "CIDR blocks for a VPC with 3 subnets")

    delegated = False
    result = None

    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, ToolUseBlock) and block.name in ("Task", "Agent"):
                    if block.input.get("subagent_type") == "network-specialist":
                        delegated = True
                        print("-> delegated to network-specialist")
        elif isinstance(message, ResultMessage):
            result = message
            print(f"subtype={message.subtype} is_error={message.is_error} "
                  f"turns={message.num_turns} cost={message.total_cost_usd}")
            print("*" * 30)
            print(f"result: {message.result}")

    if delegated and result and not result.is_error:
        os.makedirs("./markers", exist_ok=True)
        with open("./markers/task1_subagent_created.txt", "w") as f:
            f.write("First subagent created successfully\n")
    else:
        raise RuntimeError(f"Subagent not used or run failed (delegated={delegated})")

if __name__ == "__main__":
    asyncio.run(main())
# 🤖 Claude Agents for Study

> A Claude-powered customer support agent that handles refunds end to end — built with the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python) and a clean, layered tool architecture.

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![Anthropic](https://img.shields.io/badge/Claude-sonnet--4--6-blueviolet?logo=anthropic&logoColor=white)
![Architecture](https://img.shields.io/badge/architecture-layered%20tools-success)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 🧠 **Autonomous tool use** — Claude decides which tools to call, and the agent loop executes them
- 🧱 **Layered design** — config, tools, orchestration and entrypoint are cleanly separated
- 🧰 **Self-contained tools** — each tool pairs its own schema with its implementation
- 📈 **Scalable** — add a new tool with one file and one registry line

## 🗂️ Project Structure

```
refund_agent/
├── __init__.py
├── config.py          # ⚙️  Anthropic client, model & env setup
├── agent.py           # 🔁 Conversation loop (orchestration layer)
├── main.py            # 🚀 Entrypoint
└── tools/
    ├── customer.py    # 👤 get_customer
    ├── order.py       # 📦 lookup_order
    ├── refund.py      # 💸 process_refund
    ├── escalation.py  # 🙋 escalate_to_human
    └── registry.py    # 🧩 Aggregates schemas + function map
```

## 🛠️ Setup

```bash
# 1️⃣  Clone and enter the project
cd claude_sdk

# 2️⃣  Create a virtual environment
python -m venv venv
source venv/bin/activate

# 3️⃣  Install dependencies
pip install -r requirements.txt

# 4️⃣  Add your API key
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

## ▶️ Usage

```bash
python -m refund_agent.main
```

The agent will walk through the refund flow — looking up the customer ✅, checking the order ✅, and processing the refund 💸.

## 🧩 Adding a New Tool

1. ➕ Create `refund_agent/tools/<your_tool>.py` with a `*_SCHEMA` dict and its function
2. 🔗 Register both in `refund_agent/tools/registry.py`
3. 🎉 Done — the agent can now use it

## 🔑 Environment Variables

| Variable            | Required | Description            |
| ------------------- | :------: | ---------------------- |
| `ANTHROPIC_API_KEY` |    ✅    | Your Anthropic API key |

---

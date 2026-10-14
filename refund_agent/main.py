from .agent import run_conversation


def main():
    messages = [
        {
            "role": "user",
            "content": (
                "Hi, my email is alex@example.com. "
                "I want a refund for order ORD-1001 because the keyboard arrived damaged."
            )
        }
    ]

    final_text = run_conversation(messages)
    print(final_text)


if __name__ == "__main__":
    main()

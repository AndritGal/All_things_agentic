from chat import ChatModule


def main():

    chat = ChatModule()

    print("=== Collaborative Partner ===")
    print("Type 'exit' to stop.\n")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "exit":
            break

        response = chat.send_message(user_message)

        print(f"Agent: {response}\n")


if __name__ == "__main__":
    main()
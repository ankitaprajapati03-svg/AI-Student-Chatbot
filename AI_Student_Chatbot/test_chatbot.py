from chatbot import get_response

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    answer = get_response(question)

    print("Chatbot:", answer)
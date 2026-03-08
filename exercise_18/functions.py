def show_messages(text_messages):
    for text_message in text_messages:
        print(f"Show text messages: {text_message}")

def send_messages(text_messages, sent_messages):
    while text_messages:
        messages = text_messages.pop()
        print(f"\tPrinting sent messages: {messages}")
        sent_messages.append(messages)

text_messages = ['Hello my dear', 'Can we have dinner together']
sent_messages = []

show_messages(text_messages)
send_messages(text_messages, sent_messages)

text_messages = ['Hello my dear', 'Can we have dinner together']
sent_messages = []
show_messages(text_messages)
send_messages(text_messages[:], sent_messages)
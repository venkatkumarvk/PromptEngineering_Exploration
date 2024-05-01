from tkinter import *
import nltk
from nltk.chat.util import Chat, reflections

#query
business_chat_pairs = [
    (r'hello|hi|hey', ['Hello, how can I assist you today?']),
    (r'(.*) (schedule|arrange) (meeting|appointment)', ['Sure, when would you like to schedule the meeting?']),
    (r'(set|create) (reminder|task) for (.*)', ['Reminder set for %3.']),
    (r'(.*) (product|service) details', ['Sure, could you please specify which product or service you are interested in?']),
    (r'(company|business) policies', ['Our company policies include...']),
    (r'(help|support)', ['How can I assist you with support?']),
    (r'bye|goodbye', ['Goodbye! Feel free to reach out anytime if you need assistance.']),
    # if you want add more comment this section in similar manner
]

class BusinessAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Business Assistant Chatbot")
        self.txt = Text(root)
        self.txt.grid(row=0, column=0, columnspan=2)
        self.e = Entry(root, width=100)
        self.e.grid(row=1, column=0)
        self.send_button = Button(root, text="Enter for Response", command=self.send_response)
        self.send_button.grid(row=1, column=1)
        self.chatbot = Chat(business_chat_pairs, reflections)

    def send_response(self):
        user_input = self.e.get().lower()
        response = self.chatbot.respond(user_input)
        self.display_message("You -> " + user_input)
        self.display_message("Business Assistant -> " + response)
        self.e.delete(0, END)

    def display_message(self, message):
        self.txt.insert(END, "\n" + message)

if __name__ == "__main__":
    root = Tk()
    assistant = BusinessAssistant(root)
    root.mainloop()

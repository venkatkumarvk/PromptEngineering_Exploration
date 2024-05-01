from tkinter import *
import nltk
from nltk.chat.util import Chat, reflections

# query
pairs = [
    ['(hi|hello|hey)', ['Hello!', 'Hi there!', 'Hey!',]],
    ['how are you?', ['I am doing well, thank you.', 'I am good, how about you?']],
    ['(troubleshooting|troubleshoot|issue)', ['To troubleshoot your issue, please provide details about the problem you are experiencing.']],
    ['(installation|install)', ['For installation assistance, please follow the steps outlined in the installation guide provided with the software.']],
    ['(configuration|configure)', ['To configure the software, you can refer to the configuration settings in the software interface or documentation.']],
    ['(system requirements|requirements)', ['The system requirements for the software are [list of system requirements]. Please ensure your system meets these requirements for optimal performance.']],
    ['(updates|update)', ['To check for updates, you can go to the settings menu within the software and look for the option to check for updates.']],
    ['(best practices|best practice)', ['For best practices, we recommend [list of best practices]. Following these practices can help optimize your experience with the software.']],
    ['(escalate|human support)', ['If you have a complex issue that cannot be resolved by the chatbot, you can escalate the issue to our human support team. Please provide your contact information and a brief description of the issue.']],
    ['(bye|goodbye|see you later)', ['Goodbye!', 'Take care!', 'See you later!']],
]

class TechSupportChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Tech Support Chatbot")
        self.create_widgets()
        self.chatbot = Chat(pairs, reflections)

    def create_widgets(self):
        self.txt = Text(self.root)
        self.txt.grid(row=0, column=0, columnspan=2)
        self.e = Entry(self.root, width=100)
        self.e.grid(row=1, column=0)
        self.send_btn = Button(self.root, text="Send", command=self.send_message)
        self.send_btn.grid(row=1, column=1)

    def send_message(self):
        user_input = self.e.get()
        self.txt.insert(END, "\nYou: " + user_input)
        response = self.chatbot.respond(user_input)
        self.txt.insert(END, "\nBot: " + response)
        self.e.delete(0, END)

root = Tk()
app = TechSupportChatbot(root)
root.mainloop()

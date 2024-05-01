from tkinter import *
import nltk
from nltk.chat.util import Chat, reflections

# query
pairs = [
    ['(hi|hello|hey)', ['Hello!', 'Hi there!', 'Hey!',]],
    ['how are you?', ['I am doing well, thank you.', 'I am good, how about you?']],
    ['(project planning|planning)', ['Project planning involves defining project goals, creating a timeline, and allocating resources. How can I assist you further?']],
    ['(task management|tasks)', ['Task management includes assigning tasks, setting deadlines, and tracking progress. How can I assist you with your tasks?']],
    ['(resource allocation|resources)', ['Resource allocation involves assigning resources such as manpower, budget, and equipment to tasks. How can I help you allocate resources effectively?']],
    ['(progress tracking|progress)', ['Progress tracking helps monitor project milestones and identify potential delays. How can I assist you in tracking progress?']],
    ['(guidance|help)', ['Sure, I can provide guidance on project management best practices and tools. What specific aspect of project management do you need help with?']],
    ['(bye|goodbye|see you later)', ['Goodbye!', 'Take care!', 'See you later!']],
]

class ProjectManagementChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Management Support Chatbot")
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
app = ProjectManagementChatbot(root)
root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
import random

#Knowledge base

responses = {
    "hello": ["Hi there! It's Elish.", "Hello! I am Elish. How can i help you?", "Hey! Myself Elish. Whats up?"],
    "how are you":["I'm doing great!", "Feelin like a bot should - awesome!", "All good thanks for asking!"],
    "bye": ["Goodbye Amaan!", "See you later Amaan!", "Have a great day Amaan!"],
    "my name is amaan": ["Hey Amaan! It's pleasure to meet you. I'm your Elish."],
}

def get_response(user_message):
    user_msg= user_message.lower()
    for key in responses:
        if key in user_msg:
            return random.choice(responses[key])
    return "Sorry, I don't understand."

def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
     return
    
    chat_window.insert(tk.END, "You: "+user_msg +"\n","user")
    entry.delete(0, tk.END)

    bot_message = get_response(user_msg)
    chat_window.insert(tk.END, "Bot: "+ bot_message +"\n","bot")

#GUI satup
root = tk.Tk()
root.title("PyBot-Chatbot")
root.geometry("450x550")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.pack(pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=5, side=tk.LEFT, padx=(5))

send_btn = tk.Button(root, text="send", command=send_message, width=10, bg="lightblue")
send_btn.pack(pady=5, side=tk.LEFT)

root.mainloop()
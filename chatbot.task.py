# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:50:10 2026

@author: gatpa
"""

# Basic Chatbot using Python

def chatbot():
    print(" Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        
        elif user_input == "what is your name":
            print("Bot: I am a simple chatbot.")
        
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        
        else:
            print("Bot: Sorry, I don't understand.")

# Run chatbot
chatbot()
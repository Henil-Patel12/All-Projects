import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hi!']],
    ['what is your name?', ['My name is Chatbot.', 'I am Chatbot.']],
    ['how are you?', ['I am good. How about you?', 'I am doing well, thank you.']],
    ['what can you do?', ['I can help you with your queries. How may I assist you today?']],
    ['bye|goodbye', ['Goodbye!', 'Have a nice day.']],
    ['(.*)', ['Sorry, I did not understand that. Can you please repeat?']]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()

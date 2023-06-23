import spacy
import random

nlp = spacy.load("en_core_web_sm")

# Define the chatbot's responses to various user intents
responses = {
    "greetings": ["Hello!", "Hi there!", "Hey, how can I help?"],
    "goodbyes": ["Goodbye!", "Have a nice day!", "Bye!"],
    "thanks": ["You're welcome!", "No problem.", "Anytime!"],
    "affirmatives": ["Got it.", "Understood.", "Sure thing."],
    "negatives": ["I'm sorry, I didn't understand.", "Can you clarify that?", "I'm not sure what you mean."]
}

# Define some sample user intents and queries
intents = {
    "greetings": ["Hello", "Hi there", "Hey", "What's up", "Good morning"],
    "goodbyes": ["Goodbye", "Bye", "See you later", "Take care"],
    "thanks": ["Thank you", "Thanks", "Appreciate it", "Grateful"],
    "requests": ["Can you help me", "I need some assistance", "Could you assist me with", "Can you provide me with"],
    "confirmations": ["Yes", "Yeah", "Sure", "OK", "Alright"],
    "negations": ["No", "No thanks", "Not really", "I'm good"]
}

# Define a function to extract the user's intent from their query
def extract_intent(query):
    doc = nlp(query)
    for token in doc:
        if token.text.lower() in intents["greetings"]:
            return "greetings"
        elif token.text.lower() in intents["goodbyes"]:
            return "goodbyes"
        elif token.text.lower() in intents["thanks"]:
            return "thanks"
        elif token.text.lower() in intents["requests"]:
            return "requests"
        elif token.text.lower() in intents["confirmations"]:
            return "confirmations"
        elif token.text.lower() in intents["negations"]:
            return "negations"
    return None

# Define a function to generate a response based on the user's intent
def generate_response(intent):
    if intent is None:
        return random.choice(responses["negatives"])
    else:
        return random.choice(responses[intent])

# Define a function to handle a user query
def handle_query(query):
    intent = extract_intent(query)
    response = generate_response(intent)
    return response

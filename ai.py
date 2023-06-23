import random

# Define a function to get a random response
def get_response(input):
    responses = [
        "I'm sorry, I don't understand.",
        "Please elaborate.",
        "Can you rephrase that?",
        "That's interesting. Tell me more.",
        "I'm not sure what you mean.",
        "Let's change the subject.",
        "I'm not programmed to answer that.",
        "I don't have an answer for you.",
        "How does that make you feel?",
        "Tell me more about yourself.",
        "What do you think about that?",
    ]
    return random.choice(responses)

# Main loop to get user input and generate response
while True:
    input_text = input("You: ")
    response = get_response(input_text)
    print("AI: " + response)

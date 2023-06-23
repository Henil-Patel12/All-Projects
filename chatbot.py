#The AI chatbot will prompt the user to input a destination, and based on the user's input, it will take the user to a park, a beach, or a restaurant. If the user inputs a destination that the chatbot does not recognize, the chatbot will display a message indicating that it does not understand the destination.

def chatbot():
    print("Hi, I'm a chatbot. I can take you to different destinations.")
    destination = input("Where would you like to go? (park, beach, restaurant): ")
    if destination == "park":
        print("You're heading to the park. Have a great time!")
    elif destination == "beach":
        print("You're heading to the beach. Enjoy the sun and the waves!")
    elif destination == "restaurant":
        print("You're heading to the restaurant. Bon appétit!")
    else:
        print("Sorry, I don't understand your destination.")
chatbot()

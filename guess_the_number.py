import random

def play_game():
  print("Let's play a game of Guess the Number!")
  print("I'm thinking of a number between 1 and 100.")
  target_number = random.randint(1, 100)
  number_of_guesses = 0

  while True:
    guess = int(input("What's your guess? "))
    number_of_guesses += 1
    
    if guess == target_number:
      print(f"You got it in {number_of_guesses} tries!")
      break
    elif guess < target_number:
      print("The number I'm thinking of is higher.")
    else:
      print("The number I'm thinking of is lower.")

play_game()
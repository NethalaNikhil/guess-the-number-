#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random
end_game = False
print(art.logo)
print("Welcome to the number guessing game !")
print("I'm thinking number between 1 and 100")
guess = random.randint(1,101)
print("psst,the correct answer is",guess)
level = input("choose a difficulty type.Type 'easy' or 'hard' ").lower()
def game(level):
  if level == "easy":
    attemps = 10
  else:
    attemps = 5
  while not end_game:
    print(f"you have {attemps} attemps remaining to guess a number ")
    n_guess = int(input("Make a guess "))
    if n_guess== guess:
      print("You got the answer was: ",n_guess)
    elif n_guess < guess:
      print("Too low \nguess again")
      attemps -= 1
    elif n_guess > guess:
      print("Too high \nguess again")
      attemps -= 1
    if attemps == 0:
      return True
a = game(level)
end_game = a

    
  

import random

def rock_paper_scissors():
  print("Welcome to Rock, Paper, Scissors!")
  
  choices = [ "Rock", "Paper", "Scissors"]
  
  players_choice = input("Choose Rock, Paper, or Scissors: ")
  computers_choice = random.choice(choices)
  
  print(f"you chose = {players_choice}")
  print(f"computer chose = {computers_choice}" )

  if players_choice == computers_choice:
    print("It's a tie !")
  elif players_choice == "Rock" and computers_choice == "Scissors":
    print("You win!")
  elif players_choice == "Paper" and computers_choice == "Rock":
    print("You win")
  elif players_choice == "Scissors" and computers_choice == "Paper":
    print("You win!")
  else:
    print("You lose!")

rock_paper_scissors()

print("Goodbye! Thanks for playing!")

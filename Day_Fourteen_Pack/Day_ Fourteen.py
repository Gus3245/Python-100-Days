#Introduction & Program Requirements for the Higher Lower Game
import random
from Art import logo, vs
from Game_Data import data
#Create a mini DB for Compareted 
"""
#Def Compare
def Compare_A(Number):
    global Compareted_Number_B
    Compare_name = data[Number]["name"]
    Compare_Description = data[Number]["description"]
    Compare_County = data[Number]["country"]
    Compare_follower_count = data[Number]["follower_count"]

    print(f"Compare A: {Compare_name}, {Compare_Description}, from {Compare_County}")

#Remove equals Compareteds in Game.
def Remove_equals(Number, Number2):
    global Compareted_Number_B

    while Number == Number2:
        Compareted_Change = randint(0, 15)
        Compareted_Number_B = Compareted_Change
        return Compareted_Number_B
        
Compareted_Number_A = randint(0, 5)
Compareted_Number_B = randint(0, 5)

Compare_A(Compareted_Number_A)
Remove_equals(Compareted_Number_A, Compareted_Number_B)
print(vs)
Compare_A(Compareted_Number_B)

"""

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

  
    print(logo)
    
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
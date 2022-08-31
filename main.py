############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo

#Hago una list of cards
def deal_card():
  """Returns a random cards from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  #Elijo de forma random una card
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    #A blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
    #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove(). 
  return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose"
  
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has a Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"


def play_game():  
  print(logo)
  #Vamos a asignar las tarjetas al usuario y a la computadora
  user_cards = []
  computer_cards = []
  
  is_game_over = False 
  
  #Este for corre 2 veces
  for _ in range(2):
    #La agregamos al user cards
    user_cards.append(deal_card())
    #La agregamos al computer cards
    computer_cards.append(deal_card())
  
  #Hagamos un while loop
  while not is_game_over:
    #Guardamos el score del usuario y de la computadora
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      #If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another cards, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  
  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score !=0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"your final score is: {user_score}, the computer's score is: {computer_score}")  
  print(compare(user_score, computer_score))

  


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game.
while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == "y":
  clear()
  play_game()

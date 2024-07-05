#import logo and data
from replit import clear
from art import logo
from art import vs
from game_data import data
import random

A,B=random.sample(data,2)

def sozluk(data, exclude):
  # exclude olanları çıkararak yeni liste oluştur
  remaining = [s for s in data if s != exclude]
  # bu listeden rastgele bir tane seç
  return random.choice(remaining)

total_score=0

while True:
  print(logo)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

  ask=input("Who has more followers? Type 'A' or 'B': ").upper()

  if A['follower_count'] > B['follower_count'] and  ask=='A':
    clear()
    total_score+=1
    print(f"You're right! Current score: {total_score}")
    A=B
    B=sozluk(data,A)
  elif A['follower_count'] > B['follower_count'] and  ask=='B':
    print(f"Sorry, that's wrong. Final score: {total_score}")
    
    break
  elif A['follower_count'] < B['follower_count'] and  ask=='A': 
    print(f"Sorry, that's wrong. Final score: {total_score}")
    break
  elif A['follower_count'] < B['follower_count'] and  ask=='B':
    clear()
    total_score+=1
    print(f"You're right! Current score: {total_score}")
    A=B
    B=sozluk(data,A)
import random

from word import word_list
from art import stages

chosen_word = random.choice(word_list)
lives=6

from art import logo
print(logo)

display = []

End_of_game = False

for i in range(len(chosen_word)):
  display.append("_")

while not End_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed {guess}")

  for i in chosen_word:
    if i == guess:
      display[chosen_word.index(i)] = guess
      
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives-=1
    if lives==0:
      End_of_game=True
      print("You lose.")

  print(f"{' '.join(display)}")
  
  if "_" not in display:
    
    End_of_game = True
    print("You Win")

print(stages[lives])

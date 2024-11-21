import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word = ["participant", "ourselves", "meditation"]

choosen_word = random.choice(word).lower()
# print(f"the solution is {choosen_word}")
lives = 6
display = []
for _ in range(len(choosen_word)):
    display+= "_"
print(display)

end_of_game = False
while  not end_of_game: 
    guess = input("Guess a letter:\n ").lower()
    if guess in display:
        print(f"you already guessed {guess}")
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if  letter == guess:
            display[position] = letter
        
    if guess not in choosen_word:
        print(f"You guessed wrong letter {guess}. You loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Oops ! You Loose . try again.")
    print(display)
    if "_" not in display:
        end_of_game = True
        print(f" Yay! You have guessed the word {choosen_word} correctly.")
    print(stages[lives])
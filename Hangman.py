import random

word_list = ["aardvark", "baboon", "camel", "dog", "elephant", "frog", "giraffe", "hippopotamus", "iguana", "jaguar", "kangaroo", "lion", "monkey", "narwhal", "octopus", "panda", "quokka", "rhinoceross", "squirrel", "tiger", "unicorn", "vulture", "walrus", "xenopus", "yak", "zebra"]


first_life = '''
  +---+
  |   |
  O   |
      |
      |
      |
      |
========='''

second_life = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
      |
========='''
third_life = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
      |
========='''
fourth_life = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
      |
========='''
fifth_life = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
      |
========='''
death = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
      |
========='''

life_list = [first_life, second_life, third_life, fourth_life, fifth_life, death]

word = random.choice(word_list)
empty_space = ["-"] * len(word)

lives = 6
end_of_game = False

print("Welcome to Hangman!")
print(f'{"".join(empty_space)}')
print(f"The word has {len(empty_space)} charachter")

while lives  > 0 and not  end_of_game :
  
  Letter = input("What 'Letter' Do you think this word has?\n Be carefull, you only have 6 lives to guss it right.\nYou can insert one Letter at the time otherwise you loose a live.\n").lower()
  print("You have guessed the letter: " + Letter)
  
  if len(Letter) == 1:
    if Letter in word:
      print("You have chosen a correct letter")
      for i in range(len(word)):
        if word[i] == Letter:
          empty_space[i] = Letter
      print(f'{"".join(empty_space)}')
      if "-" not in empty_space:
        end_of_game = True
        print("You won")
    else:
      print("You have chosen a wrong letter")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("gamer over you loos")
      print(f"You have {lives} lives left")
      print(f'{"".join(empty_space)}')
      print(life_list[-(lives-1)])
  else:
    print("You have guessed the letter: " + Letter)
    print("You Did not follw the instructions.\nOne life is taken from you")
    print(f'{"".join(empty_space)}')
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("gamer over you loos")
    print(life_list[-(lives-1)])

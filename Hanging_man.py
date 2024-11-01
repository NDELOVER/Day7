import random
import world_list
chosen_word=random.choice(world_list.word_list)
print(chosen_word)
len_word=len(chosen_word)
guess=""
dash=["-"]*len_word
print(''.join(dash))
max_attempt=len_word
new_max_attempt=max_attempt
already_guess=""

while "-" in dash and max_attempt > 0:
      guess=input("guess a letter: ").lower()
      if guess in already_guess:
          print("You already chose this letter before!")
          continue
      already_guess+=guess
      print(f"*****************{max_attempt}/{new_max_attempt} LIVES LEFT *****************<???>/")
      print("You guessed:", guess)
      if guess in chosen_word:
          for index, letter in enumerate(chosen_word):
              if letter == guess:
                  dash[index]=letter
          print("\n"+ ''.join(dash))
      else:
            max_attempt-=1
            print("Wrong Guess. Try again.")

if "-" not in dash:
    print("Congrats")
else:
    print("You lost")

print(''.join(dash))

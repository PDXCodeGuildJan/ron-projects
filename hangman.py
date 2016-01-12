#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["mississippi", "automobile", "classroom", "computer", "yeoman", "hospital", "projector"]
numWrong = 0
listedWord = [None]


# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words
   listLength = len(words)
   randomNum = randint(0,listLength-1)
   randomWord = words[randomNum]

   # Make the randomly selected word into a list object
   listedWord = list(randomWord)


   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   currentState = "_" * len(listedWord)
   currentState = list(currentState)

   # Print the initial state of the game
   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:
      #ask the user to guess
      guess = userGuess()

      # see if the guess is in the word, update accordingly
      currentState = updateState(guess, currentState)

      printHangperson(currentState)

   # Determine if the user won or lost, and then tell them accordingly
   if  listedWord == currentState:
      print("You win! ")
   else:
      print("You lose. ")




# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong

   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)

   # If it isn't, tell the user and update the numWrong var

   if numInWord == 0:
      #numWrong = numWrong + 1
      numWrong += 1

   # If it is, congratulate them and update the state of the game.
   #    To update the state, make sure to replace ALL the '_' with"
   #    the guessed letter.
   elif numInWord > 0:
      print("Yes, there is " + str(numInWord) + " instance of the letter " + guess + " in the word ")
      # print("Yes there is {0} of the letter {1} in the word" format(numInWord, guess))

   #while we still have letters to locate we still loop
      numFound = 0
      index = 0
      while numFound < numInWord and index < len(listedWord):

         # see if letter is in word at index
         # if at the first index the item stored in listedWord is the same as what's stored in guess
         if listedWord[index] == guess:
            currentState[index] = guess
            #numfound = numFound + 1
            numFound += 1
         # increment the index
         index += 1


   return currentState


# This helpful function prompts the user for a guess,
# accepting only single letters.
# 
#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   while len(guess) != 1:
      # user has given us too long of a a response
      # check if it is exit then exit if it is
      if guess.lower == "exit":
         exit()
      #otherwise, ask them to guess again
      else:
         guess = input("Too many characters. Please type only one letter. ")


   return guess

################# DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

# This line runs the program on import of the module
hangperson()
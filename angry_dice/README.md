# Angry Dice Game


Angry Dice is a real-time dice rolling microgame now available as a Python program. The object is to reach six (stage 3) by rolling the  dice in ascending order pairs. The player has two dice they can roll and they can lock a die (except a 6), if it rolls to something they will need. Angry Dice adds different risks/rewards to the game - the base set of Angry Dice 



## Requirements

- Write a game of Angry Dice following the flowchart below.
- Create 2 die.
- Replace the number 3 with the name "Angry Face"
- Make sure to include 3 stages.
- At Stage 1 player must roll a 1 and 2 to advance to Stage 2.
- At Stage 2 player must roll an Angry Face and a 4 to advance to Stage 3.
- At Stage 3 player must roll a 5 and 6 to win the game.
- The player can't lock a 6 unless they are on Stage 3.
- Requires the player to start at the beginning if they ever roll double Angry Faces (the 3).

- Angry Dice following this flowchart
![Angry Dice flowchart](https://raw.githubusercontent.com/PDXCodeGuildJan/ron-projects/master/angry_dice/angry_dice_flowchart.jpg)


### Programing Concepts
- Classes and Objects
- Ternary Operator
- Functional programming


#### Implementation Notes
- This version of Angry Dice only includes a Die Class.
- All files relevant to this game will reside in a directory called "angry_dice", including this README, within the students Repo.


##### Installation
- From the terminal navigate to the angry_dice directory and type `python3 angry_dice.py`

######To Do
- Display Dice as ASCII art to the console
- Add a 2nd player

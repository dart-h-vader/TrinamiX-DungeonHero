# TrinamiX-DungeonHero
A demo game written in python. Was developed in 2 hour 30 minutes. 

This is our demo game. I call it the dungeon hero.
The objective of the game is to kill the dragon and the orc before they kill you, the hero.
You start with 40 health points and the monsters (orc & dragon) keep attacking you until you die or kill the monsters.
Attacking the dragon or orc is simple. Type 'attack dragon' to attack the dragon or 'attack orc' to attack orc.

Hope you have fun playing the game similar to what I had while building it.

## Starting the game
1. Ensure you have `python3` installed on your machine. `Python3` comes pre-installed on Linux and Mac. For windows, please take a look [here]( https://phoenixnap.com/kb/how-to-install-python-3-windows)
2. Clone the repository or download the `main` branch
3. From the downloaded directory, exectue `python3 Game.py`

## Technical Notes
1. The game is tested using the happy path and not so happy path
2. With the given requirement (of health), it is difficult to score a win over the monsters. If you find the game hard, reduce the dragons strength in `Dragon.py`.
3. We have used the below standard python3 libraries
    * `threading` - To ensure the monster attacks happen on a timer
    * `sys` - To exit the program via sys.exit()
4. The project *does not* use any third party library 
5. The game is developed and tested on python3


# TODO (When having more than 2 hours)

* Move the Game Logic to a class 
* Write unit test cases as a next step
* Write/generate documentation uing `pdoc3`
* Add more features to the player and monsters

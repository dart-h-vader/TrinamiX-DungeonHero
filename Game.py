import threading # Required for timer based attack on player
import sys

from GameLogic import * #Game logic is separated into a new py file 

helpString = """This is our demo game. I call it the **Dungeon Hero**.

The objective of the game is to kill the dragon and the orc before they kill you, the hero.

You start with 40 health points and the monsters (orc & dragon) keep attacking you until you die or kill the monsters.

Attacking the dragon or orc is simple. Type 'attack dragon' to attack the dragon or 'attack orc' to attack orc.

Hope you have fun playing the game similar to what I had while building it.

**NOTE: ONCE THE GAME STARTS, THE MONSTERS ATTACK YOU IRRESPECTIVE OF YOUR ATTACK.**

Meaning, you will be killed if you do not attack the monster.
"""


print (helpString)

while True:
	beginGame = input("Type 'start' to start the game, type 'help' to get help or, to exit, type 'exit': ")

	if beginGame.lower() == "start":
		break
	elif beginGame.lower() == "help":
		print(helpString)
		continue
	elif beginGame.lower() == "exit":
		sys.exit()
	else:
		print("Sorry, that is not a valid input")
		continue


# Once the game starts, we begin the timer for the Orc attack and Dragon attack. Every 1.5 seconds, the Orc attacks the player and every 2.0 seconds
# the dragon attacks the player
threading.Timer(1.5, orcAttackPlayer).start() 
threading.Timer(2.0, dragonAttackPlayer).start()


# We wait for player input for his attack strategy and act accordingly.
# NOTE: The two monsters keep attacking even if the player does not attack leading to the death of the player
while isGameRunning() == True:
	playerAttack = input("Type 'attack dragon' to attack the dragon or 'attack orc' to attack the orc: ")

	if playerAttack.lower() == 'attack orc':
		playerAttackOrc()
	elif playerAttack.lower() == 'attack dragon':
		playerAttackDragon()

import threading # Required for timer based attack on player
import sys

# TODO: Move the logic into its own class
"""
Our entire game logic resides in this file. 

We have the following global variables to keep track of the game:
1. {orcAttackCount} - Incremented every time the Orc attacks the player
2. {dragonAttackCount} - Incremented every time the Dragon attacks the player
3. {playerIsAlreadyDead} - Boolean to keep track of the player. Set to True when his health reaches 0.
This variable ensures the game's result process does not trigger twice 
4. {playInProgress} - A Boolean that handles the game's exit strategy
5. {orcDied} - Boolean to track the Orc's death and update player if he tries to attack again.
6. {dragonDied} - Boolean to track the Dragon's death and update player if he tries to attack again.
"""

from Player import Player
from Dragon import Dragon
from Orc import Orc


orcAttackCount = 0
dragonAttackCount = 0
playerAlreadyDead = False
playInProgress = True

orcDied = False
dragonDied = False

player = Player()
dragon = Dragon()
orc = Orc()

# Returns the game progress
def isGameRunning():
	global playInProgress
	return playInProgress

# Feedback to the player on how many monster attacks happened
def printMonsterHits():
	global orcAttackCount
	global dragonAttackCount

	print("\n")
	print("You were attacked {} times by the dragon".format(dragonAttackCount))
	print("You were attacked {} times by the orc".format(orcAttackCount))

# Feedback of success and exit the game
def playerWin():
	print("\n--------------GAME OVER-------------\n")
	printMonsterHits()
	print("You won the game with {} health points remaining".format(player.health))
	sys.exit()
	
# Feedback of loss and exit the game
def playerLose():
	global orcAttackCount
	global dragonAttackCount
	print("\n--------------GAME OVER-------------\n")
	printMonsterHits()		
	print("You lost the game")
	sys.exit()

# Function to update the game progress based on the health of our three characters
def updateProgress():
	global playInProgress
	global playerAlreadyDead
	global dragonDied
	global orcDied

	if orc.health <= 0 and orcDied == False:
		orcDie()
	if dragon.health <= 0 and dragonDied == False:
		dragonDie()

	if orc.health <= 0 and dragon.health <= 0:
		playerWin()
		playInProgress = False
	elif player.health == 0:
		playerAlreadyDead = True
		playInProgress = False
		playerLose()

# Function called every 1.5 seconds when the Orc attacks the player.
# We keep an account of the total number of Orc attacks and reduce the player health by 1.
def orcAttackPlayer():
	global orcAttackCount
	global playerAlreadyDead
	global playInProgress

	if orc.health <= 0 or playInProgress == False:
		return

	if player.health > 0 and playInProgress == True:
		orcAttackCount += 1
		player.health -= 1
		threading.Timer(1.5, orcAttackPlayer).start()
	elif playerAlreadyDead == False:
		updateProgress()
	
# Function called every 2 seconds when the dragon attacks the player.
# We keep an account of the total number of Dragon attacks and reduce the player health by 2.
def dragonAttackPlayer():
	global dragonAttackCount
	global playerAlreadyDead
	global playInProgress

	if dragon.health <= 0 or playInProgress == False:
		return

	if player.health > 0 and playInProgress == True:
		dragonAttackCount += 1
		player.health -= 2
		threading.Timer(1.5, dragonAttackPlayer).start()
	elif playerAlreadyDead == False:
		updateProgress()

# Death of Orc when its health reaches <= 0
def orcDie():
	global orcDied 
	orcDied = True
	print("\nThe Orc is dead\n")
	
# Death of Dragon when its health reaches <= 0
def dragonDie():
	global dragonDied
	dragonDied = True
	print("\nThe dragon is dead\n")
	
# Function called when player attacks the Orc.
# Two health points from the Orc are deducted
def playerAttackOrc():
	if orc.health <= 0:
		print("The orc is already dead")
		return
	orc.health -= 2
	# There is a possibility that the Orc's health can be less than 0. We check for this and print 0 even if the actual health is less than 0 (eg: -1)
	print("Player attacked orc. Orc health is {}".format(0  if orc.health < 0 else orc.health)) 
	printMonsterHits()
	updateProgress()
		
# Function called when player attacks the Dragon.
# Two health points from the Dragon are deducted
def playerAttackDragon():
	if dragon.health <= 0: # No point in killing the dead. Unless... dragon zombies come up :)
		print("The dragon is already dead")
		return

	dragon.health -= 2
	# There is a possibility that the Dragon's health can be less than 0. We check for this and print 0 even if the actual health is less than 0 (eg: -1)
	print("Player attacked dragon. Dragon health is {}".format(0  if dragon.health < 0 else dragon.health))
	printMonsterHits()
	updateProgress()
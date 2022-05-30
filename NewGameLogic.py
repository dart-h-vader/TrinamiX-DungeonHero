from Player import Player
from Dragon import Dragon
from Orc import Orc
import threading # Required for timer based attack on player
import sys

"""
Our entire game logic resides in this file. 

We have the following instance variables to keep track of the game:
1. {orcAttackCount} - Incremented every time the Orc attacks the player
2. {dragonAttackCount} - Incremented every time the Dragon attacks the player
3. {playerIsAlreadyDead} - Boolean to keep track of the player. Set to True when his health reaches 0.
This variable ensures the game's result process does not trigger twice 
4. {playInProgress} - A Boolean that handles the game's exit strategy
5. {orcDied} - Boolean to track the Orc's death and update player if he tries to attack again.
6. {dragonDied} - Boolean to track the Dragon's death and update player if he tries to attack again.
"""

# Define cost of each hit by the monster and the player
DRAGON_HIT_VALUE = 3
ORC_HIT_VALUE = 1
PLAYER_HIT_VALUE = 2

class NewGameLogic(object):
	player = Player()
	dragon = Dragon()
	orc = Orc()

	"""docstring for GameLogic"""
	def __init__(self):
		super(NewGameLogic, self).__init__()
		self.playInProgress = True
		self.playerAlreadyDead = False
		self.dragonDied = False
		self.orcDied = False
		self.gameRunning = True
		self.orcAttackCount = 0
		self.dragonAttackCount = 0
		
# Feedback to the player on how many monster attacks happened
	def printMonsterHits(self):
		print("\n")
		print("You were attacked {} times by the dragon".format(self.dragonAttackCount))
		print("You were attacked {} times by the orc".format(self.orcAttackCount))

# Feedback of success and exit the game
	def playerWin(self):
		print("\n--------------GAME OVER-------------\n")
		self.printMonsterHits()
		print("You won the game with {} health points remaining".format(self.player.health))
		sys.exit()

# Feedback of loss and exit the game
	def playerLose(self):
		print("\n--------------GAME OVER-------------\n")
		self.printMonsterHits()		
		print("You were killed by the monsters. You lost the game.")
		sys.exit()

		# Returns the game progress
	def isGameRunning(self) -> bool:
		return self.playInProgress

# Function to update the game progress based on the health of our three characters
	def updateProgress(self):
		if self.orc.health <= 0 and self.orcDied == False:
			print("Orc died")
			self.orcDie()
		if self.dragon.health <= 0 and self.dragonDied == False:
			print("Dragon died")
			self.dragonDie()

		if self.orc.health <= 0 and self.dragon.health <= 0:
			self.playerWin()
			self.playInProgress = False
		elif self.player.health == 0:
			self.playerAlreadyDead = True
			self.playInProgress = False
			self.playerLose()

# Death of Orc when its health reaches <= 0
	def orcDie(self):
		self.orcDied = True
		print("\nThe Orc is dead\n")

# Death of Dragon when its health reaches <= 0
	def dragonDie(self):
		self.dragonDied = True
		print("\nThe dragon is dead\n")

# Function called when player attacks the Orc.
# Two health points from the Orc are deducted
	def playerAttackOrc(self):
		if self.orc.health <= 0:
			print("The orc is already dead")
			return
		self.orc.health -= PLAYER_HIT_VALUE
		# There is a possibility that the Orc's health can be less than 0. We check for this and print 0 even if the actual health is less than 0 (eg: -1)
		print("Player attacked orc. Orc health is {}".format(0  if self.orc.health < 0 else self.orc.health)) 
		self.printMonsterHits()
		self.updateProgress()

# Function called when player attacks the Dragon.
# Two health points from the Dragon are deducted
	def playerAttackDragon(self):
		if self.dragon.health <= 0: # No point in killing the dead. Unless... dragon zombies come up :)
			print("The dragon is already dead")
			return

		self.dragon.health -= PLAYER_HIT_VALUE
		# There is a possibility that the Dragon's health can be less than 0. We check for this and print 0 even if the actual health is less than 0 (eg: -1)
		print("Player attacked dragon. Dragon health is {}".format(0  if self.dragon.health < 0 else self.dragon.health))
		self.printMonsterHits()
		self.updateProgress()

# Function called every 1.5 seconds when the Orc attacks the player.
# We keep an account of the total number of Orc attacks and reduce the player health by 1.
	def orcAttackPlayer(self):
		if self.orc.health <= 0 or self.playInProgress == False:
			return

		if self.player.health > 0 and self.playInProgress == True:
			self.orcAttackCount += 1
			self.player.health -= ORC_HIT_VALUE
			threading.Timer(1.5, self.orcAttackPlayer).start() # We start the timer again for the next attack
		elif self.playerAlreadyDead == False:
			self.updateProgress()
		
# Function called every 2 seconds when the dragon attacks the player.
# We keep an account of the total number of Dragon attacks and reduce the player health by 2.
	def dragonAttackPlayer(self):
		if self.dragon.health <= 0 or self.playInProgress == False:
			return

		if self.player.health > 0 and self.playInProgress == True:
			self.dragonAttackCount += 1
			self.player.health -= DRAGON_HIT_VALUE
			threading.Timer(1.5, self.dragonAttackPlayer).start() # We start the timer again for the next attack
		elif self.playerAlreadyDead == False:
			self.updateProgress()
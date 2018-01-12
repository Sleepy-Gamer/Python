from sys import exit
#imports the random library for using random.
import random

#ensures different results everytime using the system time.
random.seed()

def start():
	print "You have entered a dark room, the door you came from swings shut and locks."
	print "There are three doors in this room aside from the one you came from."
	print "Which door will you pick?"
	print "1, 2 or 3?"
	
	door = raw_input("> ")
	
	if door == "1":	
		print "You have chosen door 1, the door creaks open revealing the next room.\n"
		ladder_room()
	elif door == "2":
		print "You have chosen the second door. You hear the sound of heavy breathig as you walk through the door.\n"
		bear_room()
		
	elif door == "3":
		print "You have decided to go through the last door."
		print "The door is hard to open and coins spill out.\n"
		treasure_room()
	
	else:
		print "You have decided not to choose a door.\n"
		dead("The walls start to move and you are eventually crushed to death.\n")


def ladder_room():
	print "You have entered a dark room."
	print "As you wonder around you can feel a ladder but it is too dark to climb."
	print "What do you do?\n"
	action_chosen = False
	while action_chosen == False:
		print "1. Look around the room."
		print "2. Cry and wait for help."
		print "3. Try and climb the ladder."
		print "4. Go out the way you came."
		
		action = raw_input("> ")
		
		if action == "1":
			print "\nYou find a lantern and light it."
			print "You climb up the ladder safley and enter a cave up above.\n"
			action_chosen = True
			question_room()
			
		elif action == "2":
			print "\nYou hear a whisper in the wind telling you to gather courage and try again."
			action_chosen = False
			
		elif action == "3":
			print "\nAs you start to climb the ladder you don't notice the broken rings."
			dead("You fall to your death. You should not have been so foolish.")
			action_chosen = True
		elif action == "4":
			print "\nAs you push open the door you went through you scratch yourself on a poisonous nail."
			dead("You slowly die and your body turns to dust.")
			action_chosen = True
			
		else:
			print "Please select an option."
			action_chosen = False
		
def bear_room():
	print "\nAs you enter the room you notice that the heavy breathing belongs to a bear! You have woken it and need to act fast!"
	print "There is a small music sheet in the corner."
	print "There is a slope going into a cave behind the bear."
	print "\nWhat do you do?"
	print "1. Sing to the bear from the sheet."
	print "2. I don't know how to read the sheet! I will sing anything!!"
	print "3. Scream and run for the slope."
	
	action = raw_input("> ")
	
	if action == "1":
		print "\nThe bear falls asleep and you are able to slowly walk up the slope to the cave.\n"
		question_room()
	elif action == "2":
		print "\nThe bear gets drowsy, now is your chance to run!"
		live = ["2", "4", "6" ]
		die = ["1", "3", "5"]
		print "You must pick a number between 1 and 6 to see if you get to safety!"
		choice = raw_input("> ")
		if choice == live[0 or 1 or 2]:
			print "\nWell done! You get to the cave and the bear gives up!"
			question_room()
		elif choice == die[0 or 1 or 2]:
			print "\nOh no! The bear catches you before you get to safety!"
			dead("The bear spends a long time slowly tearing you limb from limb")
		else:
			print "\nThat's not a valid number."
			dead("The bear has caught you and slowly eats you.")
	
	elif action == "3":
		print "\nThe bear catches you without seeming to move."
		print "You quickly realise this was a really bad idea."
		dead("The bear slowly eats you, your bones eventually get discarded on a pile in the corner.")
		
def treasure_room():
	print "\nAs you push open the door you see piles and piles of gold coins!"
	print "In the center of the room is a note with a dice."
	print "The note reads. Roll this dice, if you get a 4 or more you will pass on to the next room."
	print "riches beyond your imagination will await you at home."
	print "However, roll a 3 or less and death will surely take you."
	print "\nWhat do you choose to do?"
	print "1. Roll the dice and await my fate!"
	print "2. Run out the way you came, death won't find you there!"
	print "3. Sit and wait, maybe there is another way?"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "\nYou pick up the dice and roll it."
		print "Dice rolling...."
		dice = random.randrange(1,7)
		
		if dice >=4:
			print dice
			print "\nWell done, you survive, the gold vanishes and shows you a door out."
			astral_plane()
		
		elif dice <=3:
			print "\nYou have rolled a ", dice, "the gold vanishes and the room gets dark."
			print "You can hear you teeth chattering as a cold hand takes yours and leads you away."
			dead("You are now with death.")
		
		else:
			print "\nThere seems to be an error in the dice."
	
	elif choice == "2":
		print "\nBefore you get to the door the room suddenly gets cold."
		print "You feel a presence in the room."
		dead("You are now with death")
		
	elif choice == "3":
		print "\nAs you sit there and wait you notice a door on the otherside."
		print "\nWhat do you want to do?"
		print "1. Climb over the treasure taking a few coins and try the door."
		print "2. Climb over the treasure ignoring the coins and try the door."
		print "3. Why bother? It's only going to be locked anyway."
		
		door = raw_input("> ")
		
		if door == "1":
			print "\nThe second you put the treasure in your pocket the whole room shakes."
			dead("You slowly die under the weight of all the coins.")
		elif door == "2":
			print "\nYou wheren't greedy! The door opens and you fall."
			dead("You fall into the void. Forever floating.")
		elif door == "3":
			dead("\nYou eventually waste away wishing you where brave enough to roll the dice.")
		else:
			dead("You eventually waste away wishing you where brave enough to roll the dice.")
			
def question_room():
	print "\nYou have entered a room with a question box in it."
	print "As you approach the box a small mechanical sound starts and paper comes out."
	print "You pick up the paper, it says:"
	print "\nWelcome traveler! You have got this far! I now have a question for you!"
	print "Where do you scratch a woozle to make it relax?"
	print "1. It's ears. \n2. It's nose \n3. It's neck?"
	
	answer = raw_input("> ")
	
	if answer == "1":
		print "\nI am afraid not. Good bye"
		dead("The floor falls from underneath you.")
	elif answer == "2":
		print "\nI am afraid not. Good bye"
		dead("The floor falls from underneath you.")
	elif answer == "3":
		print "\nYou are correct! Pass brave traveler and be rewarded."
		astral_plane()
	else:
		print "\nWhat kind of answer is that?"
		dead("The floor falls from underneath you.")
		
		
def astral_plane():
	print "\n\nCongratulations! You have reached the end of the game!"
	print "If you wen via the treasure room you are rich!"
	print "Otherwise, well, your the same as you where but alive!"
	print "Thank you for playing. You are now condemmed to this room."
	print "Maybe one day someone will find you"
	
		
		
def dead(why):
	print why
	exit(0)
start()

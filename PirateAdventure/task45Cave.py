from random import randint 
import time 


class Cave(object):

	swing_types = [
						"You lift your sword and take a swing at the bear.",
						"You hold onto your sword and swing again.", 
						"You are in pain and yet manage to lunge at the bear.",
						"You take another swipe at the bear. Is it nearly dead?",
						"You swing at the bear hoping this will hit."]
						
	def cave_start(self):

		print "You enter a cave and sit down to rest."
		print "The bandit gives you one last look"
		print "'Good luck friend, may you find that which you seek'"
		print "'Remember the woozles'"
		print "You are sorry to see him go, the company was nice."
		print "As you catch your breath you look around the cave."
		print "There seems to be a small passageway with something on the floor."
		print "After a few minutes you walk down deep into the cave towards the passageway."
		print "You see a trapdoor on the floor and go towards it."
		print "All of a sudden you hear a noise behind you and whirl around."
			
		

	
	def fight(self):
						
		print "You see a huge brown bear come towards you."
		print "The bear comes up to you baring it's teeth, it doesn't seem happy to see you."
		print "Your only choice seems to be to try and kill it."
		print "What do you do? Run or stand and fight?"
		
		#Attach health points to the two characters.
		bear = 13
		player = 10
		
		action = raw_input("> ")
		
		if action == "run":
			print "You try and run deeper into the passageway."
			print "This makes the bear very angry."
			print "The bear easily catches up to you and you stumble into a corner."
			print "The bear starts to swipe at your face and you scream in agony."
			print "You can feel your warm blood running down your body and soaking your clothing."
			print "As you fall to the ground, you find yourself laying in"
			print "a pile of skeletons. Swords and bags litter the ground."
			print "Is this what your Uncle was trying to tell you?"
			print "To be brave?"
			return 'death'
			
		elif action == "fight":
			sword_swing = randint(1, 5)
			bear_swing = randint(1, 3)
			
			
			while bear > 3 or player > 1:
				print Cave.swing_types[randint(0, len(self.swing_types)-1)]
				print "You hit the bear for %d health points" % sword_swing
				bear = bear - sword_swing
				print "The bear takes a swipe at you!"
				print "The bear hits you for %d health points\n" % bear_swing
				player = player - bear_swing
				time.sleep(1)
				
				#print "You now have %d health." % player
				#print "The bear now has %d health.\n" % bear 
	
			if bear < 3:
				print "You have seriously hurt the bear and it turns to run away."
				print "You are a compasionate person and you don't want to kill the bear."
				print "You allow it to leave the cave and go on with your journey."
				print "You go towards the trap door, heave up the creaky wooden door and go down the rope ladder."
				return 'passageway'
					
			elif player < 2:
				print "The bear swipes at you one last time."
				print "You are exhausted and hurt all over."
				print "You suddenly wish you had stayed at home."
				print "You know that it is all over and that there is nothing else you can do."
				print "You feel sorry for the wounds that you gave the bear."
				print "You slowly close your eyes and know that all is ay an end."
				return 'death'
	
			else:
				print "There seems to be an error."
		
		else:
			print "I do not understand that."
			play = Cave()
			play.fight()
			



class Home(object):
	
	def home_story(self):
		print "Hello and welcome to this game!"
		print "What is your name?"
		
		name = raw_input("> ")
		print "\nHello %s" %name 
		
		print "%s, this adventure begins in your home." %name 
		print "You have just discovered a letter from your recently"
		print "deceased Uncle explaining what happened to your family."
		print "\nIt reads: "
		print name+","
		print "I am sorry that I was unable to tell you this before but it was to protect"
		print "your life. Your parents were not killed in a freak storm like you"
		print "have been led to believe but were brave adventurers who traveled the world."
		print "They were killed by some men who were trying to find an anceint relic."
		print "This relic is now yours to look after."
		print "You must find it and protect it at all costs!"
		print "Remember the family words!"
		print "Woozles are the fuzziest companions."
		print "Now, this is what you must do."
		print "Go into the woods and find the cave, if you are worthy of the legacy"
		print "your parents left you, you will find your inheritance. "
		print "Otherwise, you will die."
		print "And it won't be quick either. Seriously,"
		print "I hope you have been paying attention to the lessons I taught you. "
		print "Anyway, there is a man here trying to break down the door."
		print "I think time has come to an end, I leave you with this advice."
		print "What ever you do, when you see the bear, dont......" 
		print "\n"
		print "The letter stops suddenly.\n\n"
		
	def item_collection(self):
		print "On the table next to the letter is a sword."
		print "You take the belt and put it on, suprised that it fits."
		print "You vaguly remember some sword fighting games that your Uncle used to play with you."
		print "Was that so that you were ready for this moment?"
		print "What do you want to do?"
		print "Go to the forest, look around, or cry?"
		
		action = raw_input("> ")
		
		if action == "forest":
			gold_taken = False 
			print "\nYou gather yourself and lace up your boots"
			print "You take one last look at the house before you leave."
			print "Will you ever return?"
			return 'go_to_forest'
			
		elif action == "look":
			gold_taken = True 
			print "\nYou look around the room and see several items."
			print "You pick up a bar of gold and some rope."
			print "Maybe these will come in handy later."
			print "You place them in your bag, lace up your boots and set off to the forest."
			return 'go_to_forest and have gold'
			
			
			
		elif action == "cry":
			print "\nYou sit down in your favourite chair."
			print "You just cannot believe this burden that has been dumped on you."
			print "You silently start crying."
			print "In a matter of moments, you are sobbing loudly."
			print "You never hear the door open."
			print "A man creeps into the house, knife in hand."
			print "He can hear you wailing pitifully and is disgusted. He knew your parents well."
			print "He creeps up behind you and slices your throat."
			return 'death'
			
		else:
			print "\n\n\nI do not understand that."
			print "~~~~~~~~~~~~~~~\n\n"
			play = Home()
			play.item_collection()
			

import time 

class Forest(object):
	def forest_start(self):
		print "\n\nYou walk into the dense forest a few miles from your home."
		print "You can hear sounds all around you, birds chirping, trees blowing in the wind,"
		print "and the sound of your footsteps crunching over the dried twigs."
		print "You have come to this forest many times during your life, but have never seen a cave."
		print "You know from experience there are many dangers in the forest and have never really explored."
		print "You walk for many hours and it starts to get dark."
		print "Suddenly the forest doesn't seem so nice, you snag your clothes and stumble a few times."
		print "You trip and fall hard onto the leaves below you."
		#time.sleep(5)
		print "\nSuddenly hand grab you and a sack is placed on your head."
		print "You hear men talking and can catch snippets of their conversation."
		print "You get pushed along and fall alot, this seems to amuse your captors alot."
		
		time.sleep(5)
		print "\n\nYou finally come to what must only be a clearing."
		print "You can't feel anything but smooth ground under your feet."
		print "You are thrown to the ground and the bag is ripped of your head"
		print "You blink at the fire that is a few paces ahead of you,"
		print "the light is harsh after the near darkness of the bag."
		print "A man comes over to you."
		print "He has a large scar going down his face and doesn't look "
		print "like he smiles very often."
		print "He stares at you for quite a while before he decides to speak."
		#time.sleep(6)
		print "\n\nHis voice is very low and you strain to hear him."
		print "'Who are you? Why were you walking in the forest?'"
		print "You are unsure what to reply and are a bit frightened."
		print "Suddenly the man just smiles. 'Don't be scared' he says"
		print "For some reason you are reasured by this."
		print "All of a sudden you tell the man everything, the letter, your quest."
		print "He seems unfazed by this story."
		print "'I knew your parent's' he says. 'I know where this cave you seek is.'"
		print "'Do you have something on you that you would give us for trade?'\n\n" 
		time.sleep(5)
		
	def have_gold(self):
		print "You tell the man that you have a gold bar."
		print "Without even thinking you hand it over."
		print "'That was very trusting of you' he says with a small smile."
		print "'I will allow you to go on with your quest.'"
		print "'I will take you to the cave, but I must leave you"
		print "at the door, it is not my destiny to continue.'" 
		print "'Come we must leave at once.'"
		print "You stand up and pick up your bag, "
		print "they left you with the sword round your hips." 
		print "The man walks ahead and you go with him.\n\n"
		time.sleep(2)
		return 'cave'
		
	def no_gold(self):
		print "You tell the man that you have nothing to offer."
		print "The man looks upset by that."
		print "'I will ask you a question'"
		print "'If you can answer this question I will take you to the cave.'"
		print "'What is the favourite food of a woozle?'"
		print "'A pear, a carrot or a lump of cheese.'\n"
		
		answer = raw_input("> ")
		
		if answer == "carrot":
			print "You are correct, well done."
			print "'I will allow you to go on with your quest.'"
			print "'I will take you to the cave, but I must leave you"
			print "at the door, it is not my destiny to continue.'" 
			print "'Come we must leave at once.'"
			print "You stand up and pick up your bag, "
			print "they left you with the sword round your hips." 
			print "The man walks ahead and you go with him.\n\n"
			time.sleep(2)
			return 'cave'
			
		elif answer == "pear":
			print "'Why would it be a pear?'"
			print "'Perhaps you are not who I thought you were.'"
			print "You hear a rustle behind you."
			print "You must have said something wrong."
			print "You feel a cold blade accrross your neck, and warm liquid spill down you."
			print "You slowly feel cold, and your eyes grow hazy.\n\n"
			
		elif answer == "cheese":
			print "'That is not corret, I am sorry friend.'" 
			print "'I have to let you go. I will not be showing you the way.'"
			print "The men all walk away and turn their backs."
			print "You go off in the forest alone." 
			print "A few hours later you trip and break your ankle."
			print "You trip and few times and just lay on the floor."
			print "You eventually freeze to death.\n\n"
			
		else:
			print "I do not understand that"
			banana = Forest()
			banana.no_gold()
			

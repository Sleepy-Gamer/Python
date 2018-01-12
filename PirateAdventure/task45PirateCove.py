import time 

class PirateCove(object):
	
	def Cove_start(self):
		print "You walk through the door and cannot believe what you can see."
		print "You have walked into a small cove surrounded by high mountains."
		print "There are ships in the water with anchors holding them in place."
		print "They are covered in seaweed and other plant life."
		print "It doesn't look like they have moved in a long time."
		print "You go to explore, thinking there is no one around."
		print "You look around the cove and see that there are chests and chests of treasure."
		print "Could the item that you are looking for be amogst it?"
		print "How will you know, will you recognise it?"
		print "You go over to the chests and start looking through them."
		print "You simply cannot believe the wealth that has been left there."
		print "Whilst you sort through the treasure, people slowly come off the ships and walk towards you."
		print "They surround you and draw small swords."
		print "Suddenly you hear the squark of a parrot!"
		print "You spin around and are confronted with a dozen sword tips in your face."
		print "'What are you doing ere?' says a scared man."
		print "The parrot settles on his shoulder and squarks again."
		print "You try and speak but cannot remember how to form words."
		print "Eventually you manage to stutter that you are following a "
		print "letter from your uncle and that a bandit who knew your "
		print "parents led you to a cave where you battle a bear and let it run away"
		print "and that if it quite okay you would like to just take the stolen relic"
		print "and go home."
		time.sleep(2)
		print "The man stares are you for several seconds."
		time.sleep(2)
		print "'Hmmmmm' he says."
		print "'How do we here know you didn't steal that information that led you here?'"
		print "'I know! What makes the fuzziest companion?'"
		
		answer = raw_input("> ")
		
		if answer == "woozles":
			print "'Yes sonny. You are who you say you are.'"
			print "'The inheritance you are looking for is a medalion.'"
			print "'It is a pirate medalion. That is what we here are'"
			print "'Do you want to join us sonny? Travel as your parent's did?'"
	
			answer = raw_input("> ")
			
			if answer == "yes":
				print "'Good choice! Here, let me put this round your neck.'" 
				print "'You are one of us now, welcome to the family.'"
				print "'SQUARK'"
				print "'Polly thinks you made the right choice.'"
				print "'Come now, we have much to do.'"
				
				print "~~~~~~~~~~~~~~~~~~~~~\n\n"
				print "I hope you enjoyed this game!"
				print "Thank you for playing!"
				
			elif answer == "no":
				print "'That there is a right shame sonny.'"
				print "'We be asking you to leave now.'"
				print "The pirates glare at you and you turn away."
				print "You go back though the door and travel up the passageway."
				print "You forget all about the bear and it amushes you are you open the trap door."
				print "You wonder why you where too scared to claim your legacy."
				
				print "~~~~~~~~~~~~~~~~~~~~~\n\n"
				print "I hope you enjoyed this game!"
				print "Thank you for playing!"
				
			else:
				print "Error"
				
		
		else:
			print "'You are not who you say you are.'"
			print "'We must protect the sectret of this place.'"
			print "'I am sorry sonny, but this is your end.'"
			print "You see the pointy ends come towards you at a startling speed."
			print "You slowly fall to the ground."
			print "It is a shame you didn't know more about woozles."
				
			print "~~~~~~~~~~~~~~~~~~~~~\n\n"
			print "I hope you enjoyed this game!"
			print "Thank you for playing!"
				
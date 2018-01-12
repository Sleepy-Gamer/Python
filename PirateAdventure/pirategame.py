from sys import exit
from random import randint 
import time 



class Sceane(object):
	
	def enter(self):
		print "You enter a sceane."
		have_gold = True 
		Sceane.have_gold = False 
		
		exit(1)

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		#set the scene to the opening scene for start of play.
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			print "\n-------------"
			#import the next scene name into a variable.
			next_scene_name = current_scene.enter()
			#change the current scene to the scene in the next scene variable.
			current_scene = self.scene_map.next_scene(next_scene_name)		 


class Home(Sceane):
	def enter(self):
		import task45Home 
		from task45Home import Home
		#from task45Home import item_collection
		play = Home()
		play.home_story()
		#play.item_collection()
		rv = task45Home.Home()
		return_value = rv.item_collection()
		if return_value == 'go_to_forest and have gold':
			Sceane.have_gold = True 
			return 'forest'
		if return_value == 'go_to_forest':
			Sceane.have_gold = False 
			return 'forest'
	
class Forest(Sceane):
	def enter(self):
		from task45Forest import Forest
		play = Forest()
		play.forest_start()
		if Sceane.have_gold == True:
			play.have_gold()
			return 'cave'
		elif Sceane.have_gold == False:
			#play.no_gold()
			return_value = play.no_gold()
			if return_value == 'cave':
				return 'cave'
		else:
			print "There is a problem, gold is lost in a void."
		
		
		
class Cave(Sceane):
	def enter(self):
		from task45Cave import Cave
		play = Cave()
		play.cave_start()
		return_value = play.fight()
		if return_value == 'passageway':
			return 'passageway'

class Hidden_Passageway(Sceane):
	def enter(self):
		print "You start to walk down a passageway."
		print "The floor is sandy and there are small pebbles everywhere."
		print "The walls are wet, and you can smell... the sea?"
		print "You walk for hours, or has it only been minutes."
		print "You sleep a while and then continue walking."
		print "After a very long walk, you come accross a simple wooden door."
		print "The door look relativly new and has a simple latch."
		print "You lift the latch and open the door."
		print "Sounds and smells assult you."
		print "You can hear sea birds calling and the sea smells a lot stronger."
		print "Taking a deep breath, you open the door wider and step through."
		time.sleep(3)
		return 'pirates'
		
class Pirate_Cove(Sceane):
	def enter(self):
		from task45PirateCove import PirateCove
		play = PirateCove()
		play.Cove_start()
		
		
class Map(object):

	scenes = {
			  #Assign the return strings to the classes.
			  'home': Home(),
			  'forest': Forest(),
			  'cave': Cave(),
			  'passageway': Hidden_Passageway(),
			  'pirates' : Pirate_Cove()
			  }
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('home')
a_game = Engine(a_map)
a_game.play()
		
		
		
#play = Home()
#play.enter()
			


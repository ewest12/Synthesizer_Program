import pygame
import random

# play a WAV file
class NotePlayer:
	"""A class to handle note playing functions"""
	# constructor
	def __init__(self, ap_settings):
		pygame.mixer.pre_init(44100, -16, 1, 2048)
		pygame.mixer.init()
		#pygame.init()
		self.notes = {}	
		self.ap_settings = ap_settings
	# add a note
	def add(self, fileName):
		#print(filepath + fileName)
		self.notes[fileName] = pygame.mixer.Sound(self.ap_settings.wav_filepath 
								+ fileName)
	# play a note
	def play(self, fileName):
		try:
			self.notes[fileName].play()
		except:
			print(fileName + ' not found!')
	def playRandom(self):
		"""play a random note"""
		index = random.randint(0, len(self.notes)-1)
		note = list(self.notes.values())[index]
		#return note
		note.play()

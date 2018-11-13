import pygame.font
import time

class PianoKey():

	def __init__(self, ap_settings, screen, key_name, keymapname):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.name = key_name
		self.keymapname = keymapname

		# Set the dimensions and properties of the pianot key
		#create the key type if it's a whole note
		if "#" not in key_name:
			self.width = ap_settings.key_width_w
			self.height = ap_settings.key_height_w
			self.key_color = (255, 255, 255)
			self.text_color = (0, 0, 0)
		#create the key type if it's a half step note sharp/flat
		else:
			self.width = ap_settings.key_width_b
			self.height = ap_settings.key_height_b
			self.key_color = (0, 0, 0)
			self.text_color = (238, 238, 238)
	
		self.font = pygame.font.SysFont(None, 48)
		
		# Build the piano key's rect object.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		#set the piano key's location.
		self.rect.x = 0
		self.rect.y = 0
		
		#self.rect.center = self.screen_rect.center

		msg = self.name
		# The button message needs to be prepped only once.
		self.prep_msg(msg)
	
	def prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.key_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

		
	def draw_key(self):
		# Draw a blank button and then draw message.
		self.screen.fill(self.key_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
	def update_location(self, x, y):
		self.rect.x = x
		self.rect.y = y
		self.prep_msg(self.name)
		
	def change_colors_active(self):
		#change colors
		self.text_color = (255, 0, 0)
		self.prep_msg(self.name)
		
	def change_colors_passive(self):
		# change colors back
		if "#" not in self.name:
			self.text_color = (0, 0, 0)
		else:
			self.text_color = (238, 238, 238)

		self.prep_msg(self.name)

	#def draw_rect(surface, fill_color, outline_color, rect, border=1):
	#	surface.fill(outline_color, rect)
	#	surface.fill(fill_color, rect.inflate(-border*2, -border*2))
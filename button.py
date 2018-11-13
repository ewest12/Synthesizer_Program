import pygame.font

class Button():

	def __init__(self, ap_settings, screen, msg, description):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.name = msg
		
		# Set the dimensions and properties of the button.
		#self.width = ap_settings.button_width
		#self.height = ap_settings.button_height
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		#get the width and height of the text
		self.text_width, self.text_height = self.font.size(msg)
		self.width = self.text_width + 5
		self.height = self.text_height + 5
		
		# Build the button's rect object.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		#set the buttons location.
		self.rect.x = 0
		self.rect.y = 0
		
		#self.rect.center = self.screen_rect.center
		
		#store the button's description
		self.description = description
		
		# The button message needs to be prepped only once.
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

		
	def draw_button(self):
		# Draw a blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
	def update_location(self, x, y):
		self.rect.x = x
		self.rect.y = y
		self.prep_msg(self.name)
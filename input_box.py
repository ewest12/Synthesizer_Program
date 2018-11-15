import pygame as pg

class InputBox:
	#An input box to store input URNs
	#Source: https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
	def __init__(self, x, y, w, h, text=''):
		self.COLOR_INACTIVE = (171, 170, 170)
		self.COLOR_ACTIVE = (117, 236, 106)
		self.FONT = pg.font.Font(None, 48)
		self.rect = pg.Rect(x, y, w, h)
		self.color = self.COLOR_INACTIVE
		self.text = text
		self.txt_surface = self.FONT.render(text, True, self.color)
		self.active = False

	def handle_event(self, event, stats):
		if event.type == pg.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
			if self.rect.collidepoint(event.pos):
				# Toggle the active variable.
				self.active = not self.active
			else:
				self.active = False
			# Change the current color of the input box.
			self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
		if event.type == pg.KEYDOWN:
			if self.active:
				if event.key == pg.K_RETURN:
					print(self.text)
					#store the new urn. User only needs to enter number codes 
					stats.urn = 'spotify:track:' + self.text
					#resest stats so a new spotify API call will be made
					stats.spot_api_called = False
					self.text = ''
				elif event.key == pg.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				# Re-render the text.
				self.txt_surface = self.FONT.render(self.text, True, self.color)

	def update(self):
		# Resize the box if the text is too long.
		width = max(200, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pg.draw.rect(screen, self.color, self.rect, 2)

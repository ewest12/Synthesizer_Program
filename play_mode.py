import pygame.font
from synth_stats import SynthStats

class PlayMode():
	"""A class to report play mode and other statistics information."""
	
	def __init__(self, ap_settings, screen, stats):
		"""Initialize play mode attributes."""
		self.screen = screen
		self.play_mode_screen_rect = screen.get_rect()
		self.ap_settings = ap_settings
		#self.play_mode_name = "None"
		self.stats = stats
		
		# Font settings for play mode information.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# Prepare the initial play image.
		self.prep_play_mode()
		self.prep_playing_output()
		self.show_play_info()
		
		print("Playmode: " + self.stats.play_mode)
		print("Artist: " + self.stats.playing_artist)
		print("Track: " + self.stats.playing_track)
		
	def prep_play_mode(self):
		"""Turn the mode into a rendered image."""
		play_mode_str = "Play Mode: " + self.stats.play_mode
		self.play_mode_image = self.font.render(play_mode_str, True, self.text_color,
			self.ap_settings.bg_color)
			
		# Display the play mode at the top left of the screen. under the buttons
		self.play_mode_rect = self.play_mode_image.get_rect()
		print("Play mode rect")
		print(self.play_mode_rect)
		self.play_mode_rect.left = self.play_mode_screen_rect.left + 20
		print("play mode screen rect left")
		print(self.play_mode_screen_rect.left)
		print("play mode rect")
		print(self.play_mode_rect)
		self.play_mode_rect.top = self.stats.button_height_max * 3
		print("play mode rect")
		print(self.play_mode_rect)
		print("Playmode: " + self.stats.play_mode)
		
	def show_play_info(self):
		"""Draw play mode to the  screen."""
		self.screen.blit(self.play_mode_image, self.play_mode_rect)
		self.screen.blit(self.playing_output_image, self.playing_output_rect)
		
	def prep_playing_output(self):
		"""Turn the high score into a rendered image."""
		self.playing_track = self.stats.playing_track
		self.playing_artist = self.stats.playing_artist
		playing_output_str = "Playing " + self.stats.playing_track + " by " + self.stats.playing_artist
		self.playing_output_image = self.font.render(playing_output_str, True, self.text_color,
			self.ap_settings.bg_color)
			
		# Display the artist info at at the top left screen. under play mode
		self.playing_output_rect = self.playing_output_image.get_rect()
		self.playing_output_rect.left = self.play_mode_screen_rect.left + 20
		self.playing_output_rect.top = self.stats.button_height_max * 4
		
		print("Artist: " + self.stats.playing_artist)
		print("Track: " + self.stats.playing_track)
		

	
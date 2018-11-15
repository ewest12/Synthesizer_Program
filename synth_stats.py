from song import Song

class SynthStats():
	"""Track statistics for Synthesizer"""
	
	def __init__(self, ap_settings):
		"""Initialize statistics."""
		self.ap_settings = ap_settings
		self.reset_stats()
		
		# Start all functions in passive state
		self.play_mode = ''
		self.playing_artist = ''
		self.playing_track = ''
		self.play_random = False
		self.play_chomatic = False
		self.show_spectro = False
		self.play_bad_k = False
		
		#Set general items
		self.button_height_max = 0
		self.ip_x = 20
		self.ip_y = 0
		self.ip_w = 140
		self.ip_h = 40
		
		# API Call reducing logic
		self.spot_api_called = False
		self.sp = ''
		self.urn = ''

		#initialize note playback info
		self.pitch_info = {}
		self.class_info = {}
		self.note_list = []
		self.notes_create = False
		
	
	def reset_stats(self):
		"""Initialize statistics that can change during the program."""
		self.play_random = False
		self.play_chromatic = False
		self.play_bad_k = False
		
	def init_song(self, sp, urn, ap_settings):
		"""initializes the song so it can be stored. Cuts down on API calls"""
		self.song = Song(sp, urn, ap_settings)
		
		
	

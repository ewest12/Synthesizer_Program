
class Settings():
	"""A class to store all settings for audio analysis tiems."""
	
	def __init__(self):
		"""Initialize the tools's static settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (69, 68, 68)
		
		# Authorization info
		self.client_id = 'fe2f103e32464be58710379146d91045'
		self.client_secret = '192bc5e7e3d345afa099dc04983451d0'
		self.redirect_uri = 'http://localhost/'
		self.my_username = '123638665'
		self.general_username = 'spotify'
		
		# Sample songs urns for demos
		self.sample_urns = {'MBK': 'spotify:track:7oK9VyNzrYvRFo7nQEYkWN',
							'BLRT': 'spotify:track:0n4bITAu0Y0nigrz3MFJMb',
							'BYCB': 'spotify:track:6KBYefIoo7KydImq1uUQlL',
							'ASJM': 'spotify:track:38Lf9Im0jQhAaKx8ehQM1S',
							'KTIA': 'spotify:track:7sP1vX19yRk9To0a7aJDzn',
							'MBRRN': 'spotify:track:3dho80fD9LVp471UuFHEEr',
							'NRLM': 'spotify:track:6tUgfsOa8PLkoede5nOR7D',
							'KSPNR': 'spotify:track:3Iu38l1yaKX1pHrZxL7z3B',
							'KSCMMS': 'spotify:track:3Vkx26AyBEuZEWEmey30sw',
							'FSLFL': 'spotify:track:0wpABKseNwvrzCRrCjg4zF',
							'KSPNR': 'spotify:track:3Iu38l1yaKX1pHrZxL7z3B',
							'KSCMMS': 'spotify:track:3Vkx26AyBEuZEWEmey30sw',
							'FSLFL': 'spotify:track:0wpABKseNwvrzCRrCjg4zF',
							'MJB': 'spotify:track:3FvQH46A4B37eNHjooIXcu',
							'TSSPD': 'spotify:track:0LD5KOEiegITINNgwiEwUh',
							'CWW': 'spotify:track:3DqSaYzwNA7aK5UB93wmDJ',
							'MJSC': 'spotify:track:2bCQHF9gdG5BNDVuEIEnNk',
							'FBML': 'spotify:track:2Kc8MfQZA6jDtM8vaMcc3G',
							'BFAE': 'spotify:track:375DLhrFmnn8kSa6ZcKGdQ'}

		# WAV filepath
		self.wav_filepath = 'C:/Users/Evan/Documents/Programming/python_work/audio_play/note_waves/'
		
		#set all note frequencies in a basic chromatic scale
		self.pitch_freq = {'C': 262, 'C#': 277, 'D': 293, 'D#': 311, 'E': 329, 'F': 349, 
			'F#': 370, 'G': 392, 'G#': 415, 'A': 440, 'A#': 466, 'B': 494}
		
		#define pitch class dictionary
		self.pitch_class = {'C': 0, 'C#': 1,'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6,
				'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
				
		#set keymap for keyboard mode
		self.key_map = {'a': 'C', 'w': 'C#', 's': 'D', 'e': 'D#', 'd': 'E', 
						'f': "F", 't': 'F#', 'g': 'G', 'y': 'G#', 'h': 'A', 
						'u': 'A#', 'j': 'B'}
		#set piano key items
		#for whole notes
		self.key_width_w = 30
		self.key_height_w = 100
		
		#for sharps/flats
		self.key_width_b = 40
		self.key_height_b = 30
		
		# define y coordinates for displaying basic info
		self.y_bar = 0.1
		self.y_beat = 0.2
		self.y_tatum = 0.3
		self.y_section = 0.4
		self.y_segment = 0.5
		
		# Set Button Options (button title, description)
		self.button_types = {'Bad Karaoke': 'Play a Song from Spotify', 
							'Spectrogram': "Display a Song's Sepectrogram",
							'Random': 'Play a Randomly Generated Song',
							'Chromatic': 'Play all notes in chromatic order'}
		self.button_width = 100
		self.button_height = 50
		
							

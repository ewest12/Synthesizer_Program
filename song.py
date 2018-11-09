import spotipy
from settings import Settings

class Song():
	"""a class to represent a track that has been imported"""
	# constructor
	def __init__(self, sp, urn, ap_settings):
		self.sp = sp
		self.ap_settings = ap_settings
		self.urn = urn
		# set basic track info
		track = sp.track(urn)
		self.t_name = track['name']
		self.t_artist = track['artists'][0]['name']
		
		# get track features
		self.audio_feat = sp.audio_features(urn)[0]
		self.audio_anly	= sp.audio_analysis(urn)
		
	def displayAudioFeatures(self):
		"""displays basic audio features of a song"""
		print("Artist: " + self.t_artist)
		print("Song: " + self.t_name)
		print("\nAudio Analysis: ")

		for key, value in self.audio_feat.items():
			try:
				print("\t" + key + ' ' + value)
			except:
				print("\t" + key + ' ' + str(value))
	
	# Gets its own pitch info
	def getPitchInfo(self):
		#extract audio analysis segments
		audio = self.audio_anly
		bars = audio['bars']
		beats = audio['beats']
		tatums = audio['tatums']
		sections = audio['sections']
		segments = audio['segments']

		#extract segment pitch details
		#create list of pitches
		pitches = []
		#create dictonary of pitches and x values
		pitch_times = {}
		#create list for pitch x and y values
		pitch_times_x = []
		pitch_times_y = []

		#add pitch segment pitch records to that list
		for segment in segments:
			#read in relevant pitch information
			start = segment['start']
			pitch = segment['pitches']
			num_pitches = len(pitch)
			duration = segment['duration']
			#determine segments pitch divisor
			#pitch_divisor = duration/num_pitches
			#define x passer
			#x_passer = start
			
			#determine the dominant pitch based on the 12 pitch classes
			#set pitch class determinant parameters
			index = 0
			max = 0
			pitch_int = 0
			num_ones = 0 
			
			for p in pitch:
				#log if there are more than 1 perfect matches
				if p == 1:
					num_ones =+ 1
				#if there is more than 1 perfect match, terminate the loop and log it
				if num_ones > 1:
					too_noisy = True
					print("Found one that's too noisy")
					p_int = 99
					break
				else:
					too_noisy = False
				#store the highest probabilty of a pitch class
				if p > max:
					max = p
					pitch_int = index
				else:
					pitch_int = pitch_int

				#keep tracking the index
				index += 1
			y_val = pitch_int
			pitch_times_y.append(y_val)
			
		#get other rhythm information
		#create x coordinate lists. ts = timestamp
		bar_ts = []
		beat_ts = []
		tatum_ts = []
		section_ts = []
		segment_ts = []
		#create y coordinate lists
		bar_y = []
		beat_y = []
		tatum_y = []
		section_y = []
		segment_y = []
		pitch_y = [] #y coordinate of segments as a function of pitch class integer
		#define y coordinates
		y_bar = self.ap_settings.y_bar
		y_beat = self.ap_settings.y_beat
		y_tatum = self.ap_settings.y_tatum
		y_section = self.ap_settings.y_section
		y_segment = self.ap_settings.y_segment

		#get segment coordinates for base layers
		for bar in bars:
			x = bar['start']
			bar_ts.append(x)
			bar_y.append(y_bar)
		for beat in beats:
			x = beat['start']
			beat_ts.append(x)
			beat_y.append(y_beat)
		for tatum in tatums:
			x = tatum['start']
			tatum_ts.append(x)
			tatum_y.append(y_tatum)
		for section in sections:
			x = section['start']
			section_ts.append(x)
			section_y.append(y_section)
		for segment in segments:
			#convert it to minutes
			x = segment['start']
			segment_ts.append(x)
			segment_y.append(y_segment)
		
		#create a dictionary for the return
		pitchinfo = {'track id': self.t_name + "_" + self.t_artist, 'bar ts': bar_ts,
					'bar y': bar_y, 'beat ts': beat_ts, 'beat y': beat_y, 'tatum ts': tatum_ts, 
					'tatum y': tatum_y, 'section ts': section_ts, 'section y': 
					section_y, 'segment ts': segment_ts, 'segment y': segment_y,
					'pitch values': pitch_times_y}

		return pitchinfo
		
	def pitchClassToFreq(self, pitch_info):
		"""
		Function that looks up frequencies for pitch class and converts to 
		conventional music notes and frequency values
		"""
		#create pitch list
		pitch_notes = []
		#create frequency list
		pitch_freqs = []
		
		pitch_list = pitch_info['pitch values']
		
		for pitch in pitch_list:
			#get pitch class note name
			for name, int in self.ap_settings.pitch_class.items():
				if int == pitch:
					note = name
					pitch_notes.append(note)
					break		
			for name, freq in self.ap_settings.pitch_freq.items():
				if name == note:
					hz = freq
					pitch_freqs.append(hz)				
					break
		#create dictionary for return
		pitchtransformed = {'notes': pitch_notes, 'frequencies': pitch_freqs}
		
		return pitchtransformed
		
	def getTempoRests(self, pitch_info):
		"""
		Function that determines how long a playback should rest for the 
		notes are played in the correct tempo and time signature
		"""
		s_time = self.audio_feat['duration_ms']
		tempo = self.audio_feat['tempo']
		time_sig = self.audio_feat['time_signature']
		num_beats = len(pitch_info['segment ts'])
		
		#get estimate length in minutes
		est_len = num_beats / tempo
		
		#get note length to have that many beats in that many minutes. 
		#and convert to seconds
		note_len = (est_len / num_beats) * 60
		
		return note_len

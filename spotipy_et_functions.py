# a module to contain all spotify spotipy API extract and transform functions

import spotipy
from matplotlib import pyplot as plt
from spotipy.oauth2 import SpotifyClientCredentials

from settings import Settings

def generalAuthSpotify(ap_settings):
	"""Initializes general spotify credentials"""
	scc = SpotifyClientCredentials(ap_settings.client_id, ap_settings.client_secret)
	sp = spotipy.Spotify(client_credentials_manager = scc)
	
	return sp

def getPitchInfo(urn, ap_settings, sp):
	"""Extracts a tracks pitch and rythm info"""
	#Get Track Info
	track = sp.track(urn)
	t_name = track['name']
	t_artist = track['artists'][0]['name']

	#extract audio analysis segments
	audio = sp.audio_analysis(urn)
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
		pitch_divisor = duration/num_pitches
		#define x passer
		x_passer = start
		
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
	y_bar = ap_settings.y_bar
	y_beat = ap_settings.y_beat
	y_tatum = ap_settings.y_tatum
	y_section = ap_settings.y_section
	y_segment = ap_settings.y_segment

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
	pitchinfo = {'track name': t_name, 'track artist': t_artist, 'bar ts': bar_ts,
				'bar y': bar_y, 'beat ts': beat_ts, 'tatum ts': tatum_ts, 
				'tatum y': tatum_y, 'section ts': section_ts, 'section y': 
				section_y, 'segment ts': segment_ts, 'segment y': segment_y,
				'pitch values': pitch_times_y}
	#print(pitch_times_y)
	#pitch_ys = pitchinfo['pitch values']
	#print(pitch_ys)
	#return all dectionary of extracted values
	return pitchinfo

def pitchClassToFreq(pitch_info, ap_settings):
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
		for name, int in ap_settings.pitch_class.items():
			if int == pitch:
				note = name
				pitch_notes.append(note)
				break		
		for name, freq in ap_settings.pitch_freq.items():
			if name == note:
				hz = freq
				pitch_freqs.append(hz)				
				break
	#create dictionary for return
	pitchtransformed = {'notes': pitch_notes, 'frequencies': pitch_freqs}
	
	return pitchtransformed
	
def getTracks(username, sp):
	""" A function to get tracks and info from a group of playlists"""
	
	#set limits for testing
	testlimit = 1
	#read in the playlists
	plists = sp.user_playlists(username, testlimit)
	#plists = sp.user_playlists(username)
	
	#create a track name dictionary of playlist results
	plistTracks = {}
	
	#fill dictionary with playlist results
	for plist in plists['items']:
		# Get playlist name
		plist_name = plist['name']
		print(plist_name)
		
		# Read in playlist specific info
		plist = sp.user_playlist(username, plist['id'], 
			fields = 'artist, tracks, name, duration_ms, next')
	
		# Get the tracks from the playlist
		tracks = plist['tracks']
		
		# Iterate through the tracks and load track info
		for i, item in enumerate(tracks['items']):
			# Get track info
			track = item['track']
			t_name = track['name']
			t_artist = track['artists'][0]['name']
			t_album = track['album']['name']
			t_dur = track['duration_ms']
			t_pop = track['popularity']
			#get tracks audio features if needed
			if return_dets == 'af_y':
				t_uri = track['uri']
				audio = sp.audio_features(t_uri)[0]
			else:
				audio = [0]
			
			#convert from ms to s and round to the nearest second
			t_dur_sec = t_dur//1000

			#set dictionary key
			entryname = plist_name + '_' + t_name
			
			#load info into track dictionary
			track = {'playlist': plist_name, 'name': t_name, 'artist': t_artist,
				'album': t_album, 'duration': t_dur_sec, 'popularity': t_pop,
				'audio_features': audio}
			#update main dictionary
			plistTracks[entryname] = track
		
		# rest to not trip API limit
		time.sleep(0.5)
		
	return plistTracks
	
def findDuplicates(tracks, filepath, filename):
	"""Finds duplicates in a dictinary of tracks"""
	# create a duplicate tracking dictionary
	trackDups = {}
	
	# iterate through the tracks to find duplicates
	for plist_name, track in tracks.items():	
		try:
			name = track['name']
			duration = track['duration']
			artist = track['artist']
			popularity = track['popularity']
			# look for existing entries
			if name in trackDups:
				# if a name and duration match, increment the count
				if duration == trackDups[name][0]:
					#print(name + " " + str(trackDups[duration][0]))
					count = trackDups[name][1]
					trackDups[name] = (duration, count+1, artist, popularity)
			else:
				# add dicitonary entry as tuple (duration, count)
				trackDups[name] = (duration, 1, artist, popularity)
		except:
			# ignore
			pass
	
	total_duplicates = len(tracks) - len(trackDups)
	print("Total Tracks: " + str(len(trackDups)))
	print("Total Duplicates: " + str(total_duplicates))
	
	# store duplicates as (name, count) tuples
	dups = []
	for k, v in trackDups.items():
		if v[1] > 1:
			dups.append((v[1], k))
	# save duplicates to a file
	#print("# of duplicate tracks to be saved: " + str(len(dups)))
	if len(dups) > 0:
		print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
	else:
		print("No duplicate tracks found!")
	f = open(filepath + filename, "w")
	for val in dups:
		f.write("[%d] %s\n" % (val[0], val[1]))
	f.close()

	#return values to user
	#if return_type == 'duplicate':
	#	return trackDups
	#elif return_type == 'all':
	#	return plistTracks
	
def displayAudioFeatures(urn):
	track = sp.track(urn)
	t_name = track['name']
	t_artist = track['artists'][0]['name']
	audio = sp.audio_features(urn)[0]
	#acousticness = audio['acousticness']

	print("Artist: " + t_artist)
	print("Song: " + t_name)
	print("\nAudio Analysis: \n")

	for key, value in audio.items():
		try:
			print(key + ' ' + value)
		except:
			print(key + ' ' + str(value))
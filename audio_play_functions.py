# A module containing functions related to generating audio notes, and
# playing them back in various ways

import sys, os
import time, random
import wave, argparse, pygame
import numpy as np
from collections import deque
from matplotlib import pyplot as plt
from note_player import NotePlayer
import synth_control_functions as scf

from settings import Settings
	

def writeWAVE(fname, data, ap_settings):
	"""writes notes to a WAV file"""
	# open file
	file = wave.open(ap_settings.wav_filepath + fname, 'wb')
	# WAV file parameters
	nChannels = 1
	sampleWidth = 2
	frameRate = 44100
	nFrames = 44100
	# set parameters
	file.setparams((nChannels, sampleWidth, frameRate, nFrames, 
					'NONE', 'noncompressed'))
	file.writeframes(data)
	file.close()

def generateNote(freq):
	"""generate note of given frequency using karplus-strong algorithm"""
	nSamples = 44100
	sampleRate = 44100
	N = int(sampleRate/freq)
	# initialize ring buffer
	buf = deque([random.random() - 0.5 for i in range(N)])
	# initialize samples buffer
	samples = np.array([0]*nSamples, 'float32')
	for i in range(nSamples):
		samples[i] = buf[0]
		avg = 0.996*0.5*(buf[0] + buf[1])
		buf.append(avg)
		buf.popleft()
		
	# convert samples to 16-bit values and then to a string
	# the maximum value is 32767 for 16-bit
	samples = np.array(samples*32767, 'int16')
	return samples.tostring()
	
def createNotes(ap_settings, nplayer, stats):
	"""
	Goes through a given list of notes and creates the WAV files.
	Then adds them to the player.
	"""
	print('creating notes...')
	for name, freq in ap_settings.pitch_freq.items():
		fileName = name + '.wav'
		if not os.path.exists(ap_settings.wav_filepath + fileName):
			data = generateNote(freq)
			print('creating ' + fileName + '...')
			writeWAVE(fileName, data, ap_settings)
		else:
			print('fileName already created. skipping...')
		#say notes were created
		stats.notes_create = True
		# add note to player
		nplayer.add(name + '.wav')
#ap_settings, screen, buttons, nplayer, urn, stats
		
def playSong(notes_list, pitch_info, song, ap_settings, sp, nplayer, screen, buttons, urn, stats, playmode, piano_keys, playback='it'):
	"""plays the audio fingerprint extraction from a song"""
	#make sure spectrogram isn't in use
	if stats.show_spectro == True:
		print("Error: can't use play features when spectogram is showing")
	else:
		#initialize click
		stats.play_bad_k = True
		#get all of the notes info
		times = pitch_info['segment ts']
		pitch_list = notes_list
		name = song.t_name
		artist = song.t_artist
		#indexing counter
		i = 0

		# play the notes and rest a bit
		print("Playing the song " + name + " by " + artist)
		
		#playback in "straight time"
		if playback == 'st':
			sleep_time = song.getTempoRests(pitch_info)
			for pitch in pitch_list:
				pitch_down = pitch
				piano_key = scf.check_piano_pitch(pitch_down, piano_keys)
				piano_key.change_colors_active()
				scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
				nplayer.play(pitch + '.wav')
				time.sleep(sleep_time)
				piano_key.change_colors_passive()
				scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
				#see if function should be stopped based on input
				#check for events
				scf.check_events(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys)
				if stats.play_bad_k == False:
					break
		#playback "in time" with segment time stamp	
		if playback == 'it':
			for pitch in pitch_list:
				pitch_down = pitch
				piano_key = scf.check_piano_pitch(pitch_down, piano_keys)
				piano_key.change_colors_active()
				scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
				nplayer.play(pitch + '.wav')
				sleep_time = times[(i + 1)] - times[i]
				time.sleep(sleep_time)
				piano_key.change_colors_passive()
				scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
				i = i + 1
				#see if function should be stopped based on input
				#check for events
				scf.check_events(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys)
				if stats.play_bad_k == False:
					break
		
def playRandom(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys):
	"""plays a random song wiht all the notes availabile"""
	#initialize click
	stats.play_random = True
	while True:
			#nplayer.playRandom()
			note = random.choice(list(ap_settings.pitch_freq.keys()))
			#note = ap_settings.sample_urns[key]
			#index = random.randint(0, len(ap_settings.pitch_freq)-1)
			#note = list(self.notes.values())[index]
			pitch_down = note
			piano_key = scf.check_piano_pitch(pitch_down, piano_keys)
			piano_key.change_colors_active()
			scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
			nplayer.play(note + '.wav')
		#	print("play random worked")
			# rest - 1 to 8 beats
			rest = np.random.choice([1, 2, 4, 8], 1, 
									p=[0.15,0.7, 0.1, 0.05])
			time.sleep(0.25*rest[0])
			piano_key.change_colors_passive()
			scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
			#see if function should be stopped based on input
			#check for events
			scf.check_events(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys)
			if stats.play_random == False:
				break

def playChromatic(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys):
	"""plays all available notes in the file in order"""
	#initialize click
	stats.play_chromatic = True
	for name, freq in ap_settings.pitch_freq.items():
		pitch_down = name
		piano_key = scf.check_piano_pitch(pitch_down, piano_keys)
		piano_key.change_colors_active()
		scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
		nplayer.play(name + '.wav')
		time.sleep(0.5)
		piano_key.change_colors_passive()
		scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys)
		#see if function should be stopped based on input
		#check for events
		scf.check_events(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys)
		if stats.play_chromatic == False:
			break


	

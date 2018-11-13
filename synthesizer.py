#get all necessary imports
#libraries
import sys
import pygame
from pygame.sprite import Group
#my modules
import audio_play_functions as apf
import spotipy_et_functions as spf
import audio_viz_functions as avf
import synth_control_functions as scf
#import classes
from settings import Settings
from button import Button
from note_player import NotePlayer
from song import Song
from synth_stats import SynthStats
from play_mode import PlayMode
from piano_keys import PianoKey
from input_box import InputBox

def run_program():
	# Initialize the program and create a screen object.
	pygame.init()
	ap_settings = Settings()

	screen = pygame.display.set_mode(
		(ap_settings.screen_width, ap_settings.screen_height))
	pygame.display.set_caption("Synthesizer (beta)")
	screen.fill(ap_settings.bg_color)
	
	#initialize the stats
	stats = SynthStats(ap_settings)
	#initialize URN
	stats.urn = 'random'
	#urn = 'spotify:track:4JehYebiI9JE8sR8MisGVb'
	
	# Create the group of buttons
	buttons = scf.create_buttons(ap_settings, screen, stats)
	
	#initialize the displayed play mode metrics
	playmode = PlayMode(ap_settings, screen, stats)
	playmode.prep_play_mode()
	playmode.prep_playing_output() 
	
	#initialize the input box
	x = 20
	y = stats.button_height_max * 5
	w = 140
	h = 40
	input_box = InputBox(x, y, w, h)
	
	# Create the group of piano keys
	piano_keys = scf.create_keys(ap_settings, screen, stats)
	
	# Initialize the Note Player, create notes if needed, 
	nplayer = NotePlayer(ap_settings)
	apf.createNotes(ap_settings, nplayer, stats)
	
	#start the main loop for the program
	while True:
		#check for events
		scf.check_events(ap_settings, screen, buttons, nplayer, stats, playmode, piano_keys, input_box)

		#redraw the screen
		scf.update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)

run_program()





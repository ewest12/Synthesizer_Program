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

def run_program():
	# Initialize the program and create a screen object.
	pygame.init()
	ap_settings = Settings()
	stats = SynthStats(ap_settings)
	screen = pygame.display.set_mode(
		(ap_settings.screen_width, ap_settings.screen_height))
	pygame.display.set_caption("Synthesizer (beta)")
	screen.fill(ap_settings.bg_color)
	#initialize URN
	urn = 'random'
	
	# Create the group of buttons
	buttons = scf.create_buttons(ap_settings, screen)
	
	# Initialize the Note Player, create notes if needed, 
	nplayer = NotePlayer(ap_settings)
	apf.createNotes(ap_settings, nplayer, stats)
	
	#start the main loop for the program
	while True:
		#check for events
		scf.check_events(ap_settings, screen, buttons, nplayer, urn, stats)

		#redraw the screen
		scf.update_screen(ap_settings, screen, buttons)

run_program()





import sys
import pygame
import math, random
import audio_play_functions as apf
import spotipy_et_functions as spf
import audio_viz_functions as avf
from button import Button
from song import Song
from synth_stats import SynthStats

def check_events(ap_settings, screen, buttons, nplayer, urn, stats, playmode):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		# Allows user to Quit
		if event.type == pygame.QUIT:
			pygame.quit()		
		# Allows control with keyboard
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ap_settings, screen, stats, nplayer)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event)
		# Mouse controls
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			#see which button was clicked
			button = find_which_clicked(mouse_x, mouse_y, buttons)
			#check info on that button
			#try:
			check_button(ap_settings, screen, button, buttons, nplayer, urn, stats, playmode)
			#except:
			#	print("no buttons were clicked")
			
def find_which_clicked(mouse_x, mouse_y, buttons):
	for button in buttons:
		# Determine the coordinates of the rectangle making up the button
		#get center coords
		b_x = button.rect.centerx
		b_y = button.rect.centery
		#get width and height
		b_w = button.width
		b_h = button.height
		#get x coord of vertical edges
		#half of button width
		b_w_h = b_w / 2
		#get left x and right x range
		b_x_l = b_x - b_w_h
		b_x_r = b_x + b_w_h
		#get y coord of horizontal edges
		#half of button height
		b_h_h = b_h / 2
		#get top y and bottom y range
		b_y_b = b_y - b_h_h
		b_y_t = b_y + b_h_h
		
		#check x coordinates
		if mouse_x >= b_x_l and mouse_x <= b_x_r:
			on_button_x = True
		else:
			on_button_x = False
		#check y coordinates
		if mouse_y >= b_y_b and mouse_y <= b_y_t:
			on_button_y = True
		else:
			on_button_y = False
		
		#see if the button was clicked
		if on_button_x == True and on_button_y == True:
			button_clicked = True
		else:
			button_clicked = False
			
		# if found the button return the button and break. 
		if button_clicked == True:
			print("Button " + button.name + " clicked")
			return button
			break
		
		#print(button.name)
		#print("Button X: " + str(b_x))
		#print("Button Y: " + str(b_y))
		#print("Button Width: " + str(b_w))
		#print("Button Height: " + str(b_h))
		#print("Mouse X: " + str(mouse_x))
		#print("Mouse YL " + str(mouse_y))
		#print("Button Left X Boundary: " + str(b_x_l))
		#print("Button Right X Boundary: " + str(b_x_r))
		#print("Button Top Y Boundary: " + str(b_y_t))
		#print("Button Bottom Y Boundary: " + str(b_y_b))
		#print("Clicked within X Boundary: " + str(on_button_x))
		#print("Clicked within Y Boundary: " + str(on_button_y))
		#print("Button Clicked: " + str(button_clicked))


		
def check_keydown_events(event, ap_settings, screen, stats, nplayer):
	"""Respond to keypresses."""
	if event.key == pygame.K_a:
		print("a key down")
		pitch = ap_settings.key_map['a']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_w:
		print("w key down")
		pitch = ap_settings.key_map['w']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_s:
		print("s key down")
		pitch = ap_settings.key_map['s']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_e:
		print("e key down")
		pitch = ap_settings.key_map['e']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_d:
		print("d key down")
		pitch = ap_settings.key_map['d']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_f:
		print("f key down")
		pitch = ap_settings.key_map['f']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_t:
		print("t key down")
		pitch = ap_settings.key_map['t']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_g:
		print("g key down")
		pitch = ap_settings.key_map['g']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_y:
		print("y key down")
		pitch = ap_settings.key_map['y']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_h:
		print("h key down")
		pitch = ap_settings.key_map['h']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_u:
		print("u key down")
		pitch = ap_settings.key_map['u']
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_j:
		print("j key down")
		pitch = ap_settings.key_map['j']
		nplayer.play(pitch + ".wav")
	#elif event.key == pygame.K_LEFT:
	#	print("left key down")
	elif event.key == pygame.K_SPACE:
		#used to stop any active program
		print("space key down")
		stats.reset_stats()
	elif event.key == pygame.K_q:
		print("quit button pressed")
		pygame.quit()

		
def check_keyup_events(event):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		print("Right key up")
	elif event.key == pygame.K_LEFT:
		print("Left key up")
		
def check_button(ap_settings, screen, button, buttons, nplayer, urn, stats, playmode):
	"""Detects which button was clicked and operates accordingly."""
	#button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
	#if button_clicked:
	if button.name == 'Bad Karaoke':
		print("bad karaoke was clicked")
		#change the playmode and prep
		#play_mode_name = button.name
		stats.play_mode = button.name
		print("Play mode: " + stats.play_mode)
		playmode.prep_play_mode()
		update_screen(ap_settings, screen, buttons, playmode)
		#use logic to reduce api calls
		if stats.spot_api_called == False:
			#initialize spotify authorization
			sp = spf.generalAuthSpotify(ap_settings)
			stats.sp = sp
			stats.spot_api_called = True
			#get the urn for the song
			#if no urn specificied find a random sample
			if urn == 'random' and stats.urn == '':
				samples = ap_settings.sample_urns
				key = random.choice(list(samples.keys()))
				#urn = random.choice(samples.items())
				urn = ap_settings.sample_urns[key]
				stats.urn = urn
			else:
				urn = stats.urn 
			# initialize the song and store in game stats to reduce API calls
			stats.init_song(sp, urn, ap_settings)
			#song = Song(sp, urn, ap_settings)
			song = stats.song
			stats.playing_track = stats.song.t_name
			stats.playing_artist = stats.song.t_artist
			playmode.prep_playing_output()
			update_screen(ap_settings, screen, buttons, playmode)

			# get the pitch info
			pitch_info = song.getPitchInfo()
			stats.pitch_info = pitch_info
			# convert the pitch info to notes and frquencies
			class_info = song.pitchClassToFreq(pitch_info)
			stats.class_info = class_info
			#extract the list of notes to play
			notes_list = class_info['notes']
			stats.notes_list = notes_list
			# create all of the notes
			#apf.createNotes(ap_settings, nplayer, stats)
			#play the song
			apf.playSong(notes_list, pitch_info, song, ap_settings, sp, nplayer, screen, buttons, urn, stats, playmode)
		else:
			stats.playing_track = stats.song.t_name
			stats.playing_artist = stats.song.t_artist
			playmode.prep_playing_output()
			update_screen(ap_settings, screen, buttons, playmode)
			#play the song
			apf.playSong(stats.notes_list, stats.pitch_info, stats.song, ap_settings, stats.sp, nplayer, screen, buttons, stats.urn, stats, playmode)
		
		#reset playmode
		stats.play_mode = ''
		stats.playing_track = ''
		stats.playing_artist = ''
		playmode.prep_playing_output()
		playmode.prep_play_mode()
	if button.name == 'Spectrogram':
		print("spectogram was clicked")
		#change the playmode and prep
		stats.play_mode = button.name
		playmode.prep_play_mode()
		update_screen(ap_settings, screen, buttons, playmode)
		#use logic to reduce api calls
		if stats.spot_api_called == False:
			#initialize spotify authorization
			#check for spotify authorization
			sp = spf.generalAuthSpotify(ap_settings)
			stats.sp = sp
			stats.spot_api_called = True
			#get the urn for the song
			#if no urn specificied or none not already defined find a random sample
			if urn == 'random' and stats.urn == '':
				samples = ap_settings.sample_urns
				key = random.choice(list(samples.keys()))
				#urn = random.choice(samples.items())
				urn = ap_settings.sample_urns[key]
				stats.urn = urn
			else:
				urn = stats.urn
			# initialize the song and store in game stats to reduce API calls
			stats.init_song(sp, urn, ap_settings)
			#song = Song(sp, urn, ap_settings)
			song = stats.song
			stats.playing_track = stats.song.t_name
			stats.playing_artist = stats.song.t_artist
			playmode.prep_playing_output()
			update_screen(ap_settings, screen, buttons, playmode)
			# get the pitch info
			pitch_info = song.getPitchInfo()
			stats.pitch_info = pitch_info
			# convert the pitch info to notes and frquencies
			class_info = song.pitchClassToFreq(pitch_info)
			stats.class_info = class_info
			#extract the list of notes to play
			notes_list = class_info['notes']
			stats.notes_list = notes_list
			# create all of the notes
			#apf.createNotes(ap_settings, nplayer, stats)
			#plot the graph
			#avf.plotAudio(pitch_info, class_info, 'f', True, True, True, True, True, True, True)
			avf.plotAudio(song, pitch_info, class_info, stats, 'f')
		else:
			stats.playing_track = stats.song.t_name
			stats.playing_artist = stats.song.t_artist
			playmode.prep_playing_output()
			update_screen(ap_settings, screen, buttons, playmode)
			#plot the graph
			avf.plotAudio(stats.song, stats.pitch_info, stats.class_info, stats, 'f')
		
		#reset playmode
		stats.play_mode = ''
		stats.playing_track = ''
		stats.playing_artist = ''
		playmode.prep_playing_output()
		playmode.prep_play_mode()
		
	if button.name == 'Random':
		print("Random was clicked")
		#change the playmode and prep
		stats.play_mode = button.name
		playmode.prep_play_mode()
		stats.playing_track = 'Random Song'
		stats.playing_artist = 'Synth Bot'
		playmode.prep_playing_output()
		update_screen(ap_settings, screen, buttons, playmode)
		apf.playRandom(ap_settings, screen, buttons, nplayer, urn, stats, playmode)
		#reset playmode
		stats.play_mode = ''
		stats.playing_track = ''
		stats.playing_artist = ''
		playmode.prep_playing_output()
		playmode.prep_play_mode()
	if button.name == 'Chromatic':
		print("Chromatic was clicked")
		#change the playmode and prep
		stats.play_mode = button.name
		stats.playing_track = 'Chromatic Scale'
		stats.playing_artist = 'Synth Bot'
		playmode.prep_playing_output()
		playmode.prep_play_mode()
		update_screen(ap_settings, screen, buttons, playmode)
		apf.playChromatic(ap_settings, screen, buttons, nplayer, urn, stats, playmode)
		#reset playmode
		stats.play_mode = ''
		stats.playing_track = ''
		stats.playing_artist = ''
		playmode.prep_playing_output()
		playmode.prep_play_mode()

		
def update_screen(ap_settings, screen, buttons, playmode):
	"""Update images on the screen and flip to a new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(ap_settings.bg_color)
	
	# Draw the play button if the program is inactive.
	#if not stats.game_active:
	for button in buttons:
		button.draw_button()
	
	# Draw the play mode informtion.
	playmode.show_play_info()
	
	# Make the most recently drawn screen visible.
	pygame.display.flip()
			
def create_buttons(ap_settings, screen, stats):
	"""Create a full group of buttons."""
	# Create a button and find the number of buttons in a row.
	# Spacing between each button is equal to one button width.
	print("screen width: " + str(ap_settings.screen_width))
	print("screen height: " + str(ap_settings.screen_height))
	
	#import the dictionary of button types
	buttons_to_make = ap_settings.button_types
	#create the list of buttons
	buttons = []
	#create and all of the buttons and fill the list
	for key, value in buttons_to_make.items():		
		button = Button(ap_settings, screen, key, value)
		buttons.append(button)
		#button.draw_button()
		
	#get the number of buttons to be printed
	num_buttons = len(buttons_to_make)
	#determine the max # of buttons that will fit in x,y dimensions for printing
	num_buttons_x, button_block = get_button_fit_x(ap_settings, buttons)
	max_buttons_y, button_height_max = get_button_fit_y(ap_settings, buttons)
	stats.button_height_max = button_height_max
	print("Button height max: " + str(stats.button_height_max))

	#we are printing buttons across top of screen
	#determine the starting point so that the buttons are centered
	#if the buttons will all fit on 1 row
	if num_buttons_x >= 1:
		#find the leftmost x starting coordinate
		#cut the button block in half
		button_block_half = button_block / 2
		#cut the screen in half
		screen_half = ap_settings.screen_width / 2
		#get leftmost starting coordinate
		starting_coord_x = screen_half - button_block_half
		print("starting x coordinate: " + str(starting_coord_x))
		
		#find the y coordinate for the row
		starting_coord_y = button_height_max
		
		print("starting y coordinate: " + str(starting_coord_y))
		
		#declare the number of rows
		num_rows = 1
	else:
		num_rows = math.ceil(num_buttons_x)
		print("We will need more than 1 row")
	
	#counter for tracking button number
	i = 0
	x = starting_coord_x
	y = starting_coord_y
	
	#update the button locations 
	for button in buttons:	
		button.update_location(x, y)
		#index counter
		i = i + 1
		#update x and y_values
		x += (button.width + (button.width / 4))
		print(button.name + " x coordinate: " + str(x))
		if num_rows == 1:
			y = y
			print(button.name + " y coordinate: " + str(y))
	else:
		print("Number of buttons per row exceeded")
	
	return buttons	

def get_button_fit_x(ap_settings, buttons):
	"""Gets the max number of times all buttons with spacing will fit in a row"""
	#get the available x space
	available_x_space = ap_settings.screen_width
	#determine the space for one button with .25 button spacing between
	button_space = 0
	for button in buttons:
		button_space += button.width + button.width / 4
	print("x button space: " + str(button_space))
	#get the number of buttons that will fit in the x direction with a margin on the left side
	num_buttons_fit_x = available_x_space / (button_space + 10)
	
	print("num_buttons_fit_x: " + str(num_buttons_fit_x))
	
	return num_buttons_fit_x, button_space
	
def get_button_fit_y(ap_settings, buttons):
	"""Gets the max number of button rows that will fit in the screen"""
	#get the available y space
	available_y_space = ap_settings.screen_height
	#determine the space for one button with 1 button spacing between
	button_height_max = 0
	for button in buttons:
		if button.height > button_height_max:
			button_height_max = button.height
		
	button_space = button_height_max * 2
	#get the number of buttons that will fit in the y direction
	num_buttons_fit_y = int(available_y_space / button_space)
	
	print("num_buttons_fit_y: " + str(num_buttons_fit_y))
	
	return num_buttons_fit_y, button_height_max
	

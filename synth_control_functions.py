import sys
import pygame
import math, random
#import pyperclip
import audio_play_functions as apf
import spotipy_et_functions as spf
import audio_viz_functions as avf
from button import Button
from piano_keys import PianoKey
from song import Song
from synth_stats import SynthStats
from input_box import InputBox

#https://pypi.org/project/pyperclip/

def check_events(ap_settings, screen, buttons, nplayer, stats, playmode, piano_keys, input_box):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		# Allows user to Quit
		if event.type == pygame.QUIT:
			pygame.quit()	
		# Allows control with keyboard
		elif event.type == pygame.KEYDOWN:
			#handle the input box
			if input_box.active == True:
				print("Stats URN: " + stats.urn)
				input_box.handle_event(event, stats)
				input_box.update()
				print("Stats URN: " + stats.urn)
			else:
			#handle the keyboard
				check_keydown_events(event, ap_settings, screen, buttons, stats, playmode, nplayer, piano_keys)
		elif event.type == pygame.KEYUP:
			if input_box.active == False:
			#handle the keyboard
				check_keyup_events(event, ap_settings, screen, buttons, stats, playmode, nplayer, piano_keys)
		# Mouse controls
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#check to see if input box is clicks
			input_box.handle_event(event, stats)
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if input_box.active == False:
				#see which button was clicked
				button = find_which_clicked(mouse_x, mouse_y, buttons)
				#check info on that button
				try:
					urn = stats.urn
					check_button(ap_settings, screen, button, buttons, nplayer, stats, playmode, piano_keys, input_box)
				except:
					print("no buttons were clicked. Or No internet connection detected")		
			
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

def check_piano_key(key_down, piano_keys):
	"""checks which piano key was pressed and returns it"""
	for piano_key in piano_keys:
		if key_down == piano_key.keymapname:
			return piano_key
			break
			
def check_piano_pitch(pitch, piano_keys):
	"""checks which piano key a pitch is being played for and returns it"""
	for piano_key in piano_keys:
		if pitch == piano_key.name:
			return piano_key
			break			
		
		
def check_keydown_events(event, ap_settings, screen, buttons, stats, playmode, nplayer, piano_keys):
	"""Respond to keypresses."""
	if event.key == pygame.K_a:
		print("a key down")
		key_down = 'a'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_w:
		print("w key down")
		key_down = 'w'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_s:
		print("s key down")
		key_down = 's'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_e:
		print("e key down")
		key_down = 'e'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_d:
		print("d key down")
		key_down = 'd'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_f:
		print("f key down")
		key_down = 'f'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_t:
		print("t key down")
		key_down = 't'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_g:
		print("g key down")
		key_down = 'g'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_y:
		print("y key down")
		key_down = 'y'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_h:
		print("h key down")
		key_down = 'h'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_u:
		print("u key down")
		key_down = 'u'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
		nplayer.play(pitch + ".wav")
	elif event.key == pygame.K_j:
		print("j key down")
		key_down = 'j'
		piano_key = check_piano_key(key_down, piano_keys)
		piano_key.change_colors_active()
		pitch = ap_settings.key_map[key_down]
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

		
def check_keyup_events(event, ap_settings, screen, buttons, stats, playmode, nplayer, piano_keys):
	"""Respond to key releases."""
	if event.key == pygame.K_a:
		print("a key up")
		key_up = 'a'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_w:
		print("w key up")
		key_up = 'w'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_s:
		print("s key up")
		key_up = 's'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_e:
		print("e key up")
		key_up = 'e'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_d:
		print("d key up")
		key_up = 'd'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_f:
		print("f key up")
		key_up = 'f'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_t:
		print("t key up")
		key_up = 't'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_g:
		print("g key up")
		key_up = 'g'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_y:
		print("y key up")
		key_up = 'y'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_h:
		print("h key up")
		key_up = 'h'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_u:
		print("u key up")
		key_up = 'u'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_j:
		print("j key up")
		key_up = 'j'
		piano_key = check_piano_key(key_up, piano_keys)
		piano_key.change_colors_passive()
	elif event.key == pygame.K_LEFT:
		print("Left key up")
		
def check_button(ap_settings, screen, button, buttons, nplayer, stats, playmode, piano_keys, input_box):
	"""Detects which button was clicked and operates accordingly."""
	#button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
	#if button_clicked:
	if button.name == 'Bad Karaoke':
		print("bad karaoke was clicked")
		#change the playmode and prep
		#play_mode_name = button.name
		#urn = stats.urn
		stats.play_mode = button.name
		print("Play mode: " + stats.play_mode)
		playmode.prep_play_mode()
		update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)
		#use logic to reduce api calls
		if stats.spot_api_called == False:
			#initialize spotify authorization
			sp = spf.generalAuthSpotify(ap_settings)
			stats.sp = sp
			stats.spot_api_called = True
			#get the urn for the song
			#if no urn specificied find a random sample
			if stats.urn == 'random':# and stats.urn == '':
				samples = ap_settings.sample_urns
				key = random.choice(list(samples.keys()))
				#urn = random.choice(samples.items())
				urn = ap_settings.sample_urns[key]
				#stats.urn = urn
			else:
				urn = stats.urn
			# initialize the song and store in game stats to reduce API calls
			stats.init_song(sp, urn, ap_settings)
			#song = Song(sp, urn, ap_settings)
			song = stats.song
			stats.playing_track = stats.song.t_name
			stats.playing_artist = stats.song.t_artist
			playmode.prep_playing_output()
			update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)

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
			apf.playSong(notes_list, pitch_info, song, ap_settings, sp, nplayer, screen, buttons, urn, stats, playmode, piano_keys, input_box)
		else:
			stats.playing_track = stats.song.t_name
			stats.playing_artist = stats.song.t_artist
			playmode.prep_playing_output()
			update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)
			#play the song
			apf.playSong(stats.notes_list, stats.pitch_info, stats.song, ap_settings, stats.sp, nplayer, screen, buttons, stats.urn, stats, playmode, piano_keys, input_box)
		
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
		update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)
		#use logic to reduce api calls
		if stats.spot_api_called == False:
			#initialize spotify authorization
			#check for spotify authorization
			sp = spf.generalAuthSpotify(ap_settings)
			stats.sp = sp
			stats.spot_api_called = True
			#get the urn for the song
			#if no urn specificied or none not already defined find a random sample
			if stats.urn == 'random':# and stats.urn == '':
				samples = ap_settings.sample_urns
				key = random.choice(list(samples.keys()))
				#urn = random.choice(samples.items())
				urn = ap_settings.sample_urns[key]
				#stats.urn = urn
			else:
				urn = stats.urn
			# initialize the song and store in game stats to reduce API calls
			stats.init_song(sp, urn, ap_settings)
			#song = Song(sp, urn, ap_settings)
			song = stats.song
			stats.playing_track = stats.song.t_name
			stats.playing_artist = stats.song.t_artist
			playmode.prep_playing_output()
			update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)
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
			update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)
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
		update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)
		apf.playRandom(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys, input_box)
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
		update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box)
		apf.playChromatic(ap_settings, screen, buttons, nplayer, urn, stats, playmode, piano_keys, input_box)
		#reset playmode
		stats.play_mode = ''
		stats.playing_track = ''
		stats.playing_artist = ''
		playmode.prep_playing_output()
		playmode.prep_play_mode()

		
def update_screen(ap_settings, screen, buttons, playmode, piano_keys, input_box):
	"""Update images on the screen and flip to a new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(ap_settings.bg_color)
	
	# Draw the play button if the program is inactive.
	#if not stats.game_active:
	for button in buttons:
		button.draw_button()
	
	# Draw the play mode informtion.
	playmode.show_play_info()
	
	#draw the input box
	input_box.draw(screen)
	
	#Draw the piano key
	for piano_key in piano_keys:
		piano_key.draw_key()
	
	# Make the most recently drawn screen visible.
	pygame.display.flip()

def create_input_box(ap_settings, stats):
	"""Creates the input box for urns and places it"""
	x = 20
	y = stats.button_height_max * 6
	w = 140
	h = 32
	InputBox(x, y, w, y)
	
	
	
def create_keys(ap_settings, screen, stats):
	"""Create a group of keys and display like a keyboard"""
	#create the group of keys
	keys_to_make = ap_settings.key_map
	piano_keys = []
	total_width = 0
	for key, value in keys_to_make.items():
		piano_key = PianoKey(ap_settings, screen, value, key)
		piano_keys.append(piano_key)
		total_width = total_width + piano_key.width 
		
	#find center of screen
	center_screen = ap_settings.screen_width / 2
		
	# display the keys like a keyboard
	#define the x starting value
	x = center_screen - (total_width / 2)
	#define top y value
	y = stats.button_height_max * 7
	for piano_key in piano_keys:
		#if "#" not in piano_key.name:
		piano_key.update_location(x, y)
		#else:
		#	x = x - piano_key.width / 2
		#	piano_key.update_location(x, y)
		x = x + piano_key.width 
		
	return piano_keys
	
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
	

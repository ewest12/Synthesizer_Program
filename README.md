# Synthesizer_Program
A musical synthesizer program with a few key functions: 
1. Is a stand alone program that can generate WAV files for playback, if necessary
2. Play these sounds based on mapped computer keyboard inputs
3. Display keyboard input and other "active modes" status visually
4. Have a few "fun" modes:
  a. Interface with Spotify API to play a "bad karaoke" version based on an estimate of the song's acoustic fingerprint.
    i. Song determined either by user input or a random choice from a seed of pre-chosen songs.
  b. Display an estimate "spectrogram" of the "bad karaoke" song so that the user can visually see how the song should sound
  c. Play a random song based on the available notes
  d. Play a chromatic scale

#Set up
1. Put all files in the same directory
2. Create a folder named "note_waves" in this directory
3. Put your spotify developer credentials in "settings.py"
  a. You can register and get these credentials for free at developer.spotify.com

#Current controls
1. Run the program based from "syntehsizer.py"
2. Key maps for note playback are outlined in "settings.py"
3. Pressing "space" will stop any current function
4. Pressing 'q' or clicking the exit "x" will close the program

#Known bugs
1. Program will crash if you try to click anywhere on the program if "Spectrogram" is active. You must close this window before 
    using any additional "fun modes."

#Library dependencies
1. pygame
2. sys
3. os
4. time
5. random
6. wave
7. argparse
8. numpy
9. collections
10. matplotlib
11. spotipy
12. math

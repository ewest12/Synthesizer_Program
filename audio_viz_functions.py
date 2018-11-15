from matplotlib import pyplot as plt
import numpy as np

def extractItems(item_list):
	print("x")

def gbar(ax, x, y, width = 0.5, bottom = 0):
	"""plots a gradient bar"""
	X = [[.6, 1.6], [.7, .7]]
	for left, top in zip(x,y):
		right = left + width
		ax.imshow(X, interpolation ='bicubic', cmap=plt.cm.RdYlGn,
				extent=(left, right, bottom, top), alpha=1)
	
def plotAudio(song, pitch_info, class_info, stats, pitch_type='p', s_bar=False, 
			s_beat=False, s_tatum=False, s_section=False, s_segment=False, 
			s_af=True, s_af_peaks=False):
	"""Plot any audio items in the form of an acoustic fingerprint"""
	#initialize click
	stats.play_show_spectro = True

	#note type info
	if s_af == True:
		sg_x = pitch_info['segment ts']
		if pitch_type == 'p':
			pt_y = pitch_info['pitch values']
			if s_af_peaks == True:
				plt.scatter(sg_x, pt_y, c='r', marker='o', label='pitch',s=3)
			#gradient bar chart
			width = max(sg_x)/len(sg_x)
			xmin, xmax = xlim = 0, max(sg_x)
			ymin, ymax = ylim = 0, max(pt_y)
			fig, ax = plt.subplots()
			ax.set_facecolor('xkcd:blue')
			ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)
			gbar(ax, sg_x, pt_y, width)
			ax.set_aspect('auto')
			plt.ylabel('Pitch Class', fontsize=16)
		elif pitch_type == 'f':
			pt_y = class_info['frequencies']		
			if s_af_peaks == True:
				plt.scatter(sg_x, pt_y, c='r', marker='o', label='pitch',s=3)
			#gradient bar chart
			width = max(sg_x)/len(sg_x)
			xmin, xmax = xlim = 0, max(sg_x)
			ymin, ymax = ylim = 0, max(pt_y)
			fig, ax = plt.subplots()
			ax.set_facecolor('xkcd:blue')
			ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)
			gbar(ax, sg_x, pt_y, width)
			ax.set_aspect('auto')
			plt.ylabel('Frequenc (Hz)', fontsize=16)
	#beat type info
	if s_bar == True:
		bar_ts = pitch_info['bar ts']
		bar_y = pitch_info['bar y']
		plt.scatter(bar_ts, bar_y, c='b', marker='x', label='bar', s=1)
	if s_beat == True:
		beat_ts = pitch_info['beat ts']	
		beat_y = pitch_info['beat y']
		plt.scatter(beat_ts, beat_y, c='r', marker='s', label='beat', s=1)
	if s_tatum == True:
		tatum_ts = pitch_info['tatum ts']
		tatum_y = pitch_info['tatum y']
		plt.scatter(tatum_ts, tatum_y, c='r', marker='p', label='tatum', s=1)
	if s_section == True:
		section_ts = pitch_info['section ts']
		section_y = pitch_info['section y']
		plt.scatter(section_ts, section_y, c='c', marker='D', label='section', 
					s=1)
	if s_segment == True:
		segment_ts = pitch_info['segment ts']
		segment_y = pitch_info['segment y']
		plt.scatter(segment_ts, segment_y, c='m', marker='v', label='segment', 
					s=1)


	#plot segmentation information
	width = 20
	height = 17

	fig_size = plt.rcParams["figure.figsize"]
	fig_size[0] = width
	fig_size[1] = height
	plt.rcParams["figure.figsize"] = fig_size

	plt.legend(loc='right')
	plt.legend().set_visible(False)
	title = ("Estimate Spectrogram for " + song.t_name + " by " + song.t_artist)
	plt.title(title, fontsize=24)
	plt.xlabel('Time in Seconds', fontsize=16)
	plt.tick_params(axis='x', which='major', labelsize=16)

	plt.show()
	
	#end button stat
	stats.play_show_spectro = False

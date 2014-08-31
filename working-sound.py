import sfml as sf

def play_sound():
	# load a sound buffer from a wav file
	#MAYBE LOAD SOUND INTO SOUND BUFFER, FROM THE FILE PASSED INTO from_file???
	buffer = sf.SoundBuffer.from_file("sounds/NO-high.wav")

	# create a sound instance and play it
	sound = sf.Sound(buffer)
	#play sound
	sound.play()

	# loop while the sound is playing
	#Essential piece of code, will not play without this
	while sound.status == 2:
		pass
		#print("This is the sound status:", sound.status)
		## leave some CPU time for other processes
		#sf.milliseconds = convert time into milliseconds, then have it sleep for that long
		#sf.sleep(sf.milliseconds(100))
play_sound()
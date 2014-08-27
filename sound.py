from sfml import *
def play_sound():

	buffer = SoundBuffer.from_file("NO.wav")
	
	sound = Sound()
	sound.buffer = buffer
	sound.play()

play_sound()
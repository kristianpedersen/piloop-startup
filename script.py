# Raspberry Pi: Play an audio file on startup, and loop it infinitely

# 1. Copy the code below and save it as script.py
# 2. Save your music file in the same directory
# 3. Open terminal
# 4. Enter "crontab -e"
# 5. At the bottom of the file, enter "@reboot sudo python /home/pi/script.py &"
# 6. Ctrl+X -> Y
#
# Your audio file should now play upon startup, and loop infinitely

import pygame
pygame.mixer.init()
pygame.mixer.music.load("sound.wav")
pygame.mixer.music.play(loops = -1) #loops the file infinitely
while pygame.mixer.music.get_busy() == True:
	continue
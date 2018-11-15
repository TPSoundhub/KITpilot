# HelloW2.py - 2. Program
# - Importerng af biblioteker med ekstra funktioner
# - Afspilning af 2 lyde samtidigt med hver deres volumen niveau

import pygame
import time  

l1 = "hej-1sek.wav"
l2 = "Baggrund.wav"
#
# sti til lyde paa PI - fuld sti til start fra boot
#
# l2 = "/home/pi/KITpilot-master/Baggrund.wav"
# l1 = "/home/pi/KITpilot-master/hej-1sek.wav"

# initialisering af mixer
pygame.mixer.init()

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load(l2)
pygame.mixer.music.play(0)
#
# Kan lave det samme med mindre tekst ved at skrive:
#
# Bagg=pygame.mixer.music
# Bagg.set_volume(0.1)
# Bagg.load(l2)
# Bagg.play(0)

time.sleep(5) # vent 5 sek og lyt til baggrunds lyd inden hej lyd

pygame.mixer.Sound(l1).set_volume(1.0)
pygame.mixer.Sound(l1).play()
#
# Kan lave det samme med mindre tekst ved at skrive:
#
# Lyd1=pygame.mixer.Sound(l1)
# Lyd1.set_volume(1.0)
# Lyd1.play(0)

#time.sleep(20)  # Hvis der ryddes op med quit kommer sidte lyd ikke ud.

#For at rydde op i mixer
#pygame.quit()   


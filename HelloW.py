import pygame
import time

print ("hej med jer")

# Spil lydfil hej med jer som alternativ til at skrive det
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Python_test/hej-1sek.wav")
music_volume = 1.0
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(0)

time.sleep(2) # Vent 2 sek saa lyd er afspillet - aht afvikling fra cmd linie

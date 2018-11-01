import pygame
import time

#Play sound file som baggrunds lyd
pygame.mixer.init()
music_volume = 0.1
pygame.mixer.music.load("Baggrund.wav")
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(0)


time.sleep(5) # vent 5 sek og hør baggrund

# Spiller hej med jer lyd ovenpaa baggrund - samtidigt
# benyyter en streng til at korte kommando ned
# Spiller samtidigt med music(baggrund)

sound_vol = 1.0
Sound_to_play = pygame.mixer.Sound("hej-1sek.wav")
Sound_to_play.set_volume(sound_vol)
Sound_to_play.play()

time.sleep(20)  #Vent lidt inden det slutter af aht cmd linie afvikling

pygame.quit()   # For at rydde op i lyd buffre etc.

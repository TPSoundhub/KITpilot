import pygame
import time

print ("hej med jer")

#Play sound file hej med jer som baggrunds lyd
pygame.mixer.init()
pygame.mixer.music.load("hej-1sek.wav")
music_volume = 1.0
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(0)

time.sleep(5) #Vent 5 sek

#Play sound in different way (Sound instead of music)
Sound_to_play = pygame.mixer.Sound("hej-1sek.wav")
Sound_to_play.play()

time.sleep(10)  #Vent laenge nok til at lyd er afspillet ifm cmd line


                
            
         

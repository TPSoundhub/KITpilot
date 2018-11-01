#
# HelloW2.py med 2 samtidige lyde
# Viser at der er parallelitet i afvikling mht lyd
# Selvom program er en strenget.
# Forskel i afvikling fra shell i IDLE miljoet og fra kommando linie
# - Skal have fuld sti til lyd filer for at koere fra kommando linie.
# - Lyd afvikling stopper naar program stopper fra kommandolinie. Derfor sleep!

import pygame
import time

#Play sound file som baggrunds lyd
pygame.mixer.init()
music_volume = 0.1
pygame.mixer.music.load("/home/pi/Python_test/Baggrund.wav")
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(0)


time.sleep(5) # vent 5 sek og lyt til baggrunds lyd

# Spiller hej med jer lyd ovenpaa baggrund - samtidigt
# benytter en streng til at korte kommando ned
# og bruger mixer.Sound som kan koere oveni (samtidigt med) mixer.music

sound_vol = 1.0
Sound_to_play = pygame.mixer.Sound("/home/pi/Python_test/hej-1sek.wav")
Sound_to_play.set_volume(sound_vol)
Sound_to_play.play()

time.sleep(20)  # Vent lidt inden det slutter af aht cmd linie afvikling

pygame.quit()   # For at rydde op i lyd buffre etc.

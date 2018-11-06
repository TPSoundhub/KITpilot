import pygame
import time
# sys med for at kunne stoppe via X i GUI vinduet
# IKKE noedvendig ifm headless (incl. fra boot via rc.local)!!
# Danske tegn forvirrer python fra cmd line :-)
import sys

# sti til lyde paa PI
# baggrundslyd = "/home/pi/Python_test/Baggrund.wav"
# lyd1 = "/home/pi/Python_test/Lyd1.wav"
# lyd2 = "/home/pi/Python_test/Lyd2.wav"

#Sti til lyde paa PC/MAC udelades - afvikler kun program lokalt
baggrundslyd = "Baggrund.wav"
lyd1 = "lyd1.wav"
lyd2 = "lyd2.wav"

pygame.mixer.init()

pygame.mixer.music.load(baggrundslyd)
music_volume=0.1
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(0)
music_playing = True

sound_vol = 0.5
Sound1_to_play = pygame.mixer.Sound(lyd1)
Sound1_to_play.set_volume(sound_vol)
Sound2_to_play = pygame.mixer.Sound(lyd2)
Sound2_to_play.set_volume(sound_vol)

pygame.display.init()
sceen = pygame.display.set_mode((100,100))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_UP:
                print("UP")
                if music_volume<1.0:
                    music_volume=music_volume+0.02
                    pygame.mixer.music.set_volume(music_volume)
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                if music_volume>0.0:
                    music_volume=music_volume-0.02
                    pygame.mixer.music.set_volume(music_volume)
            elif event.key == pygame.K_SPACE:
                if music_playing == True:
                    pygame.mixer.music.pause()
                    music_playing=False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif event.key == pygame.K_p:
                pygame.mixer.music.play()
            elif event.key == pygame.K_1:
                Sound1_to_play.play()
            elif event.key == pygame.K_2:
                Sound2_to_play.play()
                
# Paen oprydning - Hvis ikke import sys i starten saa fjern sidste
pygame.quit()
sys.exit()


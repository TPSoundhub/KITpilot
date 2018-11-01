import pygame
import time
# sys med for at kunne stoppe via X i GUI vinduet
# IKKE noedvendig ifm headless (incl. fra boot via rc.local)!!
# Danske tegn vil forvirre python fra cmd line :-)
import sys

pygame.mixer.init()

pygame.mixer.music.load("/home/pi/Python_test/Baggrund.wav")

pygame.mixer.music.play(0)
music_playing = True
music_volume=0.1
pygame.mixer.music.set_volume(music_volume)

sound_vol = 1.0
Sound1_to_play = pygame.mixer.Sound("Lyd1.wav")
Sound1_to_play.set_volume(sound_vol)
Sound2_to_play = pygame.mixer.Sound("Lyd2.wav")
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


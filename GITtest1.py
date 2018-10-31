# import winsound - KUN windows så ikke interessant
import pygame
import time
# sys med for at kunne stoppe via X i GUI for kørende vindue
# Ikke noedvendig ifm headless paa PI (incl fra boot via RC.local)
# Danske tegn vil forvirre Python fra cmd linie :-)
import sys
#Using module keyboard VIRKER IKKE SKAL FØRST INSTALLERES
#import keyboard 

print ("hej med jer")

    
# Play Windows exit sound.
# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

pygame.mixer.init()
#Play Mp3"
pygame.mixer.music.load("....")
pygame.mixer.music.play(0)
music_playing = True
music_volume = 0.4
pygame.mixer.music.set_volume(music_volume)

#Play wav and in different way (Sound and string constant)
#Sound_to_play = pygame.mixer.Sound("Ihd.wav")
#Sound_to_play.play()

#a=0
#b=1
#while a<8:
#    print(a)
#    a=b
#    b=a+b
#    time.sleep(2)

#i_string = raw_input("Stop med enhver tekst streng fulgt af <return>: ")
#print(""" + i_string + """ + " blev indtastet")


# Kunne ikke få installeret keyboard pakken så ?? - pip install keyboard
#while True:#making a loop
#    try: #used try so that if user pressed other than the given key error will not be shown
#        if keyboard.is_pressed('q'):#if key 'q' is pressed 
#            print('You Pressed A Key!')
#            break#finishing the loop
#        else:
#            pass
#    except:
#        break #if user pressed a key other than the given key the


#pygame event hanlding - kræver et display window med fokus så ????
pygame.display.init()
screen = pygame.display.set_mode((100 , 100))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_LEFT:
                print("left key pressed")
            elif event.key == pygame.K_UP:
                print("up key is pressed")
                if music_volume<1.0:
                    music_volume = music_volume+0.1
                    pygame.mixer.music.set_volume(music_volume)
            elif event.key == pygame.K_DOWN:
                print("down key is pressed")
                if music_volume>0.0:
                    music_volume = music_volume-0.1
                    pygame.mixer.music.set_volume(music_volume)
            elif event.key == pygame.K_RIGHT:
                print("right key is pressed")
                
            elif event.key == pygame.K_p:
                pygame.mixer.music.play()
                music_playing == True
            elif event.key == pygame.K_SPACE:
                if music_playing == True:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True

#For at rydde op inden program forlades. Hvis sys ikke importeres i starten saa fjern sys.exit
pygame.quit()
sys.exit()
                

                
            
         

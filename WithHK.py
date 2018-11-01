# Danske tegn vil forvirre python fra cmd line :-)
# Kombo af key event og keyboard
#
import pygame
import time
import RPi.GPIO as GPIO
import time

run = True

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Python_test/Baggrund.wav")
pygame.mixer.music.play(0)
music_playing = True
music_volume=0.1
pygame.mixer.music.set_volume(music_volume)

sound_vol = 1.0
Sound1_to_play = pygame.mixer.Sound("/home/pi/Python_test/Lyd1.wav")
Sound1_to_play.set_volume(sound_vol)
Sound2_to_play = pygame.mixer.Sound("/home/pi/Python_test/Lyd2.wav")
Sound2_to_play.set_volume(sound_vol)

def button_callback(channel):
    if channel == 29:
        Sound1_to_play.play()  # Sound 1 paa Gul Skal have check paa kanaler ved gentryk
    elif channel == 31:
        Sound2_to_play.play()  # Sound 2 paa Hvid
    elif channel == 18:
        pygame.mixer.music.play(0)  # Genstart baggrund på roed
        # Bør nok istedet lave en paen exit på program
        run = False # Stop program på roed

GPIO.setmode(GPIO.BOARD) # Board attribute means reference by PIN number
GPIO.setup(29,GPIO.IN)   # PIN 29 on RPi from PIN 29 on Beocreate = Gul knap
GPIO.setup(31,GPIO.IN)   # PIN 31 on RPi from PIN 31 on Beocreate = Hvid knap
GPIO.setup(18,GPIO.IN)   # PIN 18 on RPi from PIN 27 on Beocreate = Roed knap

GPIO.add_event_detect(29,GPIO.RISING,callback=button_callback) # setup event on pin 29 from low to high
GPIO.add_event_detect(31,GPIO.RISING,callback=button_callback) # setup event on pin 31 from low to high
GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback) # setup event on pin 18 from low to high



while run:
    time.sleep(5)
                
# Skal have lavet paen exit her - noget med exception og finally .....              
# Paen oprydning - Hvis ikke import sys i starten saa fjern sidste
pygame.quit()
GPIO.cleanup()



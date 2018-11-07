#
# Danske tegn forvirrer python fra cmd line i dette esetup saa derfor er de vaek :-)
# Kombo af key_event og HelloW2 til at lave kombinationn af lyd mix og knap aktivering
#
import pygame
import time
import RPi.GPIO as GPIO
import time

# sti til lyde paa PI
baggrundslyd = "/home/pi/KITpilot-master/Baggrund.wav"
lyd1 = "/home/pi/KITpilot-master/Lyd1.wav"
lyd2 = "/home/pi/KITpilot-master/Lyd2.wav"

#Sti til lyde paa PC/MAC udelades - afvikler kun program lokalt
#baggrundslyd = "Baggrund.wav"
#lyd1 = "lyd1.wav"
#lyd2 = "lyd2.wav"

run = True

pygame.mixer.init()
pygame.mixer.music.load(baggrundslyd)
pygame.mixer.music.play(0)
music_playing = True
music_volume=0.1
pygame.mixer.music.set_volume(music_volume)

sound_vol = 1.0
Sound1_to_play = pygame.mixer.Sound(lyd1)
Sound1_to_play.set_volume(sound_vol)
Sound2_to_play = pygame.mixer.Sound(lyd2)
Sound2_to_play.set_volume(sound_vol)

def button_callback(channel):
    if channel == 29:
        Sound1_to_play.play()       # Sound 1 paa Gul Skal evt have check paa kanaler ved gentryk
    elif channel == 31:
        Sound2_to_play.play()       # Sound 2 paa Hvid
    elif channel == 18:
        pygame.mixer.music.play(0)  # Genstart baggrund paa roed

        # Kunne istedet bruge det til at lave en paen exit paa program
        # Stop program paa roed med run lig false gaar ikke
        # Global variabel ikke tilgaengelig i callback

GPIO.setmode(GPIO.BOARD) # Board attribute means reference by PIN number
GPIO.setup(29,GPIO.IN)   # PIN 29 on RPi from PIN 29 on Beocreate = Gul knap
GPIO.setup(31,GPIO.IN)   # PIN 31 on RPi from PIN 31 on Beocreate = Hvid knap
GPIO.setup(18,GPIO.IN)   # PIN 18 on RPi from PIN 27 on Beocreate = Roed knap

GPIO.add_event_detect(29,GPIO.RISING,callback=button_callback) # setup event on pin 29 from low to high
GPIO.add_event_detect(31,GPIO.RISING,callback=button_callback) # setup event on pin 31 from low to high
GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback) # setup event on pin 18 from low to high

while run:
    time.sleep(5)
                
# Boer have en paen exit her - noget med exception og finally .....              
# Paen oprydning - Kommer vi aldrig til paa denne maade med koden ovenfor!!
# Kan kun stoppe program med ctrl-c eller fjerne det fra Boot seq. eller stoppe IDLE shell
# At der ikke ryddes op kan betyde at kanaler er blokeret og lyd ikke spilles naeste gang!!
# eller at tilstand paa PINs er udefineret..
pygame.quit()
GPIO.cleanup()



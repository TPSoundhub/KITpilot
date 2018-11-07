import pygame
import time

print ("hej med jer")


#demo af funktion - kan bruges til at vise debug

def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end=' ')
        a,b = b,a+b
    print()


fib(1000)   


# sti til lyde paa PI
hejlyd = "/home/pi/KITpilot-master/hej-1sek.wav"

#Sti til lyde paa PC/MAC udelades - afvikler kun program lokalt
#hejlyd = "hej-1sek.wav"

# Spil lydfil hej med jer som alternativ til at skrive det
pygame.mixer.init()
pygame.mixer.music.load(hejlyd)
music_volume = 1.0
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(0)

time.sleep(2) # Vent 2 sek saa lyd er afspillet - aht afvikling fra cmd linie

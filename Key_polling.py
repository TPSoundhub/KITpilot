#PIN polling eksempel

import RPi.GPIO as GPIO
import traceback
import time



GPIO.setmode(GPIO.BOARD) # Board attribute means reference by PIN number
GPIO.setup(29,GPIO.IN)   # PIN 29 on RPi from PIN 29 on Beocreate = Gul knap
GPIO.setup(31,GPIO.IN)   # PIN 31 on RPi from PIN 31 on Beocreate = Hvid knap
GPIO.setup(18,GPIO.IN)   # PIN 18 on RPi from PIN 27 on Beocreate = Rød knap

while(True):
    if(GPIO.input(29)==1):
        print("GUL knap lukket")
    elif(GPIO.input(31)==1):
        print("Hvid knap er lukket")
    elif(GPIO.input(18)==1):
         print("Rød knap er lukket")
    else:
        print("begge er åbne")
    time.sleep(0.5)

# Kode bliver ved til afbrydes med ctrl-c. Ikke paen kode!!!
# Efterlader GPIO pindene i udefineret tilstand!!
# bør have en afslutning som GPIO.cleanup()
# Kode bliver ved med at køre rundt og bruge CPU tid (polling)
# Som at skulle åbne front doeren hele tiden for at se om der kommer gæster
    

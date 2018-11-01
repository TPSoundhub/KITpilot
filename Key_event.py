# PIN event/interupt eksempel - til sammenligning med Key_polling eksemplet
#

import RPi.GPIO as GPIO
import time

def button_callback(channel):
    if channel == 29:
        print("GUL knap trykket ned")
    elif channel == 31:
        print("Hvid knap er trykket ned")
    elif channel == 18:
         print("Roed knap er trykket ned")

GPIO.setmode(GPIO.BOARD) # Board attribute means reference by PIN number
GPIO.setup(29,GPIO.IN)   # PIN 29 on RPi from PIN 29 on Beocreate = Gul knap
GPIO.setup(31,GPIO.IN)   # PIN 31 on RPi from PIN 31 on Beocreate = Hvid knap
GPIO.setup(18,GPIO.IN)   # PIN 18 on RPi from PIN 27 on Beocreate = Roed knap

GPIO.add_event_detect(29,GPIO.RISING,callback=button_callback) # setup event on pin 29 from low to high
GPIO.add_event_detect(31,GPIO.RISING,callback=button_callback) # setup event on pin 31 from low to high
GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback) # setup event on pin 18 from low to high


while(True):
    # her kan man lave kode hvor hoveddoeren ikke hele tiden checkes.
    # Man kan lave noget andet - naar der kommer nogen ringer de paa doeren (callback)
    # men for sammenligningens skyld lader vi her bare koden staa og skrive at der ikke er nogen
    # men kan frigive CPU i hele 5 sekunder uden at vi taber knap tryk
    
    print("alle 3 er ikke aktiveret")
    time.sleep(10)

# Kode bliver ved til afbrydes med ctrl-c. Ikke paen kode!!!
# Efterlader GPIO pindene i udefineret tilstand!!
# Boer have en afslutning som GPIO.cleanup()

    

# Import Libraries
import serial
import pygame


# Set up the Serial connection to capture the Microbit communications
# Find the right port as USB devices are identified and remembered in case they come back
# ON Windows/PC the name/number used are COM#, where # is the number - Use putty or Terra term to test
# ON Raspbian/PI the name/number is /dev/ttvACM#, where # is the number - Use Ls and full path to find the ones found and test for the right one

test_on = True
run_in_gui = True

ser = serial.Serial()                                                         
ser.baudrate = 115200
ser.port = "COM9"    # on PC/Windows
# ser.port = "/dev/ttyACM0" # On PI/Raspbian
ser.open()

def receive_char():
    # Read in a line from the Microbit, store it in variable 'microbitdata' as a string and then clean it up to only the character sent from microbit
    microbitdata = str(ser.readline())
    if test_on: print("received input: ",microbitdata)
    if run_in_gui:
        char_received = microbitdata[2:3]
    else:
        char_received = microbitdata[0:1]
    if test_on: print("treated input: ",char_received)
    return char_received


# Pygame initialising wrt sound mixer and selected sound samples - Note different paths depending on where program is executed

# include full path to sounds on PI
# baggrundslyd = "/home/pi/KITpilot-master/Baggrund.wav"
# lyd1 = "/home/pi/KITpilot-master/Lyd1.wav"
# lyd2 = "/home/pi/KITpilot-master/Lyd2.wav"

# No need for path on PC/MAC - must be located at same location as the program
baggrundslyd = "Baggrund.wav"
lyd1 = "lyd1.wav"
lyd2 = "lyd2.wav"

pygame.mixer.init()

music_volume=0.1
pygame.mixer.music.load(baggrundslyd)
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(-1)  # minus een giver infinite loop af baggrundslyd

music_playing = True

sound_vol = 0.5
Sound1_to_play = pygame.mixer.Sound(lyd1)
Sound1_to_play.set_volume(sound_vol)
Sound2_to_play = pygame.mixer.Sound(lyd2)
Sound2_to_play.set_volume(sound_vol)


# Loop forever

while True:


    rc = receive_char()
    
    if rc == "H" or rc == "h":
        if music_volume<1.0:
            music_volume=music_volume+0.02
            pygame.mixer.music.set_volume(music_volume)
            if test_on:
                print("Vol up")
                print(music_volume)
    elif rc == "V" or rc == "v":
        if music_volume>0.0:
            music_volume=music_volume-0.02
            pygame.mixer.music.set_volume(music_volume)
            if test_on:
                print("Vol down")
                print(music_volume)
    elif rc == "F" or rc == "f":
        if test_on: print("Hvad skal vi lave med en F/f ved tilt frem?")
    elif rc == "T" or rc == "t":
        if test_on: print("Hvad skal vi lave med en T/t ved tilt tilbage?")
    elif rc == "C" or rc == "c":
        if test_on: print("Hvad skal vi lave på en C/c ved pin 1 aktiveret?")
    elif rc == "0" or rc == "1" or rc == "2" or rc == "3" or rc == "4" or rc == "5" or rc == "6" or rc == "7" or rc == "8" or rc == "9":
        if test_on: print("Hvad skal vi lave på 0-9 ved pin 2 aktiveret?")
    elif rc == "A" or rc == "a":
        if test_on: print("Sound 1 on top")
        Sound1_to_play.play()
    elif rc == "B" or rc == "b":
        if test_on: print("Sound 2 on top")
        Sound2_to_play.play()
    


# Clean up after execution
# Close the serial connection
# What to close program with ??
# what othe cleaning needed ??

ser.close()
pygame.quit()



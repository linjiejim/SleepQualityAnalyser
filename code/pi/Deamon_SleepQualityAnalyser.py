'''This program is used as a deamon script running at the backgroud when raspberryPi starts.'''
# Function: 
#   1. When this program is ready after reboot, the LED will blink for 3 seconds. 
#   2. Press the Button for 3 seconds: 
#       LED on:  load the specified file(SaveDataToCsv.py). 
#       LED off: stop the specified file(SaveDataToCsv.py). 
# Note: 
#   1. register this file to /etc/rc.local
#   2. add a line at the end before 'exit 0'
#   >>    sudo -u pi python3 /home/pi/SleepQualityAnalyser/code/pi/Deamon_SleepQualityAnalyser.py


import RPi.GPIO as GPIO
import time 
import subprocess

# the program to be called
file_name = '/home/pi/SleepQualityAnalyser/code/pi/SaveDataToCsv.py'

# pins definition
PIN_BTN = 16
PIN_LED = 17

# GPIO init
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_LED, GPIO.OUT)

# global variables
btn_count = 0
led_stat = False

# ready
GPIO.output(PIN_LED, True)
time.sleep(0.5)
GPIO.output(PIN_LED, False)
time.sleep(0.5)
GPIO.output(PIN_LED, True)
time.sleep(0.5)
GPIO.output(PIN_LED, False)
time.sleep(0.5)
GPIO.output(PIN_LED, True)
time.sleep(0.5)
GPIO.output(PIN_LED, False)

# forever
while True:	
    # button state
    btn_sta = GPIO.input(PIN_BTN)

    # pressed = 0, unpressed = 1
    if btn_sta: 
       btn_count = 0
    else: 
       btn_count += 1

    # if pressed for 3 seconds
    if btn_count >= 3:
        led_stat = not led_stat

        # run subprocess
        if led_stat:
            print('On')
            GPIO.output(PIN_LED, led_stat)
            proc1 = subprocess.Popen(args=['python3', file_name])

        # stop subprocess
        else:
            print('Off')
            proc1.terminate()
            proc1.wait()

        # update LED state
        GPIO.output(PIN_LED, led_stat)
        btn_count = 0

    time.sleep(1)
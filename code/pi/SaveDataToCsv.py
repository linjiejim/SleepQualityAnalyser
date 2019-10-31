# Import packages
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO
import Adafruit_DHT

import time
import datetime
import csv

# Pins connection
PIN_DHT22 = 21
PIN_PIR = 11

PIN_ADC_CLK = 18
PIN_ADC_MISO = 23
PIN_ADC_MOSI = 24
PIN_ADC_CS = 25

PIN_ADC_BRIGHTNESS = 0
PIN_ADC_AIRQUALITY = 2
PIN_ADC_MIC = 6

# initialize MCP3008
mcp = Adafruit_MCP3008.MCP3008(clk=PIN_ADC_CLK, cs=PIN_ADC_CS, miso=PIN_ADC_MISO, mosi=PIN_ADC_MOSI)

# initialize GPIO 
GPIO.setup(PIN_PIR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# path name
filepath = '../../data/'
# file name
filename = 'sleep_'+datetime.datetime.now().strftime("%Y_%M_%d_%H:%M:%S")+".csv"
# title
title = ['Time', 'Temp', 'Humidity', 'Light', 'Noise', 'Motion', 'AirQ']

# create the header
with open(filepath+filename, 'w') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=title)
    writer.writeheader()

# insert data by row 
while True:
	# read data
	tstr = datetime.datetime.now().strftime("%H:%M:%S")
	hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_DHT22)
	light = mcp.read_adc(PIN_ADC_BRIGHTNESS)
	noise = mcp.read_adc(PIN_ADC_MIC)
	motion = GPIO.input(PIN_PIR)
	airq = mcp.read_adc(PIN_ADC_AIRQUALITY)
	
	hum = round(hum, 2)
	temp = round(temp, 2) 

	# save data
	with open(filepath+filename, 'a') as csvFile:
		writer = csv.DictWriter(csvFile, fieldnames=title)
		writer.writerow({'Time': tstr, 
			'Temp' : temp, 
			'Humidity' : hum,
			'Light': light,
			'Noise': noise,
			'Motion': motion,
			'AirQ': airq })

	# close session
	csvFile.close()

	# wait 
	time.sleep(1)

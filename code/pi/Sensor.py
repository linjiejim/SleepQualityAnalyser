
'''
Supported Sensors

* Temperature and Humidity 
* Brightness 
* Noise
* Motion
* AirQuality
'''

# Import packages
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO


import time

# Pins connection
PIN_DHT11 = 21
PIN_PIR = 11

PIN_ADC_CLK = 18
PIN_ADC_MISO = 23
PIN_ADC_MOSI = 24
PIN_ADC_CS = 25

PIN_ADC_BRIGHTNESS = 0
PIN_ADC_NOISE = 1


class Sensor:
	def __init__(self): 
		# initialize MCP3008
		mcp = Adafruit_MCP3008.MCP3008(clk=PIN_ADC_CLK, cs=PIN_ADC_CS, miso=PIN_ADC_MISO, mosi=PIN_ADC_MOSI)
		
		# initialize GPIO 
		GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		pass

	def read_temperature_humidity(self):
		return temp, humi 

	def read_brightness(self):
		return brig 

	def read_noise(self):
		return nois 

	def read_rip(motion):
		moti = GPIO.input(PIN_PIR)
		return moti 

	def read_air_quality(self):
		return airq 

	def read_adc():
		vals = [0]*8
    	for i in range(8):
        	vals[i] = mcp.read_adc(i)
		return vals

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
import Adafruit_DHT

import time

# Pins connection
PIN_DHT22 = 21
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
		humi, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_DHT22)
		#humi = int(humi * 1000) / 1000
		#temp = int(temp * 1000) / 1000
		return temp, humi 

	def read_brightness(self):
		brig = mcp.read_adc(PIN_ADC_BRIGHTNESS)
		return brig 

	def read_noise(self):
		nois = mcp.read_adc(PIN_ADC_NOISE)
		return nois

	def read_rip(motion):
		moti = GPIO.input(PIN_PIR)
		return moti 

	def read_air_quality(self):
		airq = 66
		return airq 

	def read_adc():
		vals = [0]*8
		for i in range(8):
				vals[i] = mcp.read_adc(i)
		return vals
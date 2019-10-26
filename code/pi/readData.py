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
PIN_ADC_AIRQUALITY = 2

# initialize MCP3008
mcp = Adafruit_MCP3008.MCP3008(clk=PIN_ADC_CLK, cs=PIN_ADC_CS, miso=PIN_ADC_MISO, mosi=PIN_ADC$

# initialize GPIO 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:
  humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_DHT22)
  brightness = mcp.read_adc(PIN_ADC_BRIGHTNESS)
  noise = mcp.read_adc(PIN_ADC_NOISE)
  motion = GPIO.input(PIN_PIR)
  airquality = mcp.read_adc(PIN_ADC_AIRQUALITY)
  #airquality = 666 ## havent supportted 

  # print the data collected
  print('Collected Data: \n \
    Temperature:{}\n \
    Humidity:{}\n \
    Brightness:{}\n \
    Noise:{}\n \
    Motion:{}\n \
    AirQuality:{}\n'.format(temperature,\
      humidity,\
      brightness,\
      noise,\
      motion,\
      airquality))

  # sleep for 1 second 
  time.sleep(0.1)
  


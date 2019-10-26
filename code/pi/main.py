import Sensor

ss = Sensor()

while True:

  # read data from sensors
  temperatrue, humidity = ss.read_temperature_humidity()
  brightness = ss.read_brightness()
  noise = ss.read_nosie()
  motion = ss.read_rip()
  airquality = ss.read_air_quality()

  # print the data collected
  print('Temperature:{}\n \
    Humidity:{}\n \
    Noise:{}\n \
    Motion:{}\n \
    AirQuality:{}\n'.format(temperatrue,\
      humidity,\
      brightness,\
      noise,\
      motion,\
      airquality))

  # sleep for 1 second 
  time.slepp(1)
  
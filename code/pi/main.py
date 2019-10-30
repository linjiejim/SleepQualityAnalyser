from Sensor import Sensor

import mysql.connector
import datetime
import time 

mydb = mysql.connector.connect(
  host="novice-tech.cotmblgcxfwk.ap-southeast-2.rds.amazonaws.com",
  user="noviceTech",
  password="Novicetech5047",
  database="novicetech"
)
ss = Sensor()

cursor = mydb.cursor()
cursor.execute("TRUNCATE SleepData")

while True:

  # read data from sensors
  temperatrue, humidity = ss.read_temperature_humidity()
  brightness = ss.read_brightness()
  noise = ss.read_nosie()
  motion = ss.read_rip()
  airquality = ss.read_air_quality()

  # store data to AWS RDS Mysql
  insert_stmt = (
    "INSERT INTO SleepData(SleepDataDateTime, SleepDataTemp, SleepDataHumid, "
    "SleepDataBright, SleepDataNoise, SleepDataMotion, SleepDataAir) "
    "VALUES(%s, %s, %s, %s, %s, %s, %s)"
  )
  data = (datetime.datetime.now(), temperature, humidity, brightness,
          noise, motion, airquality)
  cursor.execute(insert_stmt, data)

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
  time.sleep(1)
  

import datetime
import redis
import serial
import time

db = redis.Redis()

with serial.Serial(port     = "/dev/ttyUSB0",
                   baudrate = 9600,
                   parity   = serial.PARITY_NONE,
                   stopbits = serial.STOPBITS_ONE,
                   bytesize =serial.EIGHTBITS,
                   timeout  = 1) as arduino:
  time.sleep(0.1)
  if arduino.isOpen():
    while True:
      arduino.write("READ".encode())
      answer = arduino.readline().decode('utf-8').rstrip()
      if answer != "":
        request_key = "windData:"+datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        request_value = answer
        db.set(request_key, request_value)
        arduino.flushInput()
        break

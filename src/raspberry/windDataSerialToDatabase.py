import datetime
import redis
import serial

# Connection to the Redis database
db = redis.Redis()

# Create the serial listener
ser = serial.Serial(
 port='/dev/ttyUSB0',
 baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)

while True:

  # Create the key for the database
  # Format: windData:timestamp
  request_key = "windData:"+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

  # Get the value of the sensor
  x = ser.readline().decode('utf-8').rstrip()
  request_value = x

  # Insert data into the Redis database
  db.set(request_key, request_value)

import time
import os

hostname = '127.0.0.1:5432'

response = os.system("ping -c 1 " + hostname)

while response != 0:
  print("Looking for postgres...")
  time.sleep(5)
  response = os.system("ping -c 1 " + hostname)
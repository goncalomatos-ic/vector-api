import time
import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("POSTGRES_IP"))

postgres_ip = '' + os.getenv("POSTGRES_IP")
hostname = postgres_ip + ':5432'

response = os.system("ping -c 1 " + hostname)

while response != 0:
  print("Looking for postgres...")
  time.sleep(5)
  response = os.system("ping -c 1 " + hostname)
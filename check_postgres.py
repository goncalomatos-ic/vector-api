import time
import os
from dotenv import load_dotenv
load_dotenv()

response = os.system("ping -c 1 " + os.getenv("POSTGRES_IP"))

while response != 0:
  print("Looking for postgres...")
  time.sleep(5)
  response = os.system("ping -c 1 " + os.getenv("POSTGRES_IP"))
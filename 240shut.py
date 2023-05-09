# SUTDOWN COMPUTER EVERY 2 HOURS
import os
import time

# Number of seconds in 240 hours
shutdown_time = 240 * 60 * 60

while True:
    # Wait for 240 hours
    time.sleep(shutdown_time)

    # Shutdown the computer
    os.system('shutdown /s /t 1')


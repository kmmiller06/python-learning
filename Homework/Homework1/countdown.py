# Countdown
import time

print("Countdown starting...")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # Waits 1 second between numbers
print("Blast off!")
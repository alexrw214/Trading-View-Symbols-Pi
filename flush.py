import time
import sys
ERASE_LINE = '\x1b[;2K'

for j in range(0,20):
	for i in range(1,4):
		sys.stdout.write("Waiting for market to open"+"."*i+"\r")
		sys.stdout.flush()
		time.sleep(0.5)
		sys.stdout.write(ERASE_LINE)
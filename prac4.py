# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#placeholder import for now
import time
import threading
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


#SETUP
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
ADC = AnalogIn(mcp, MCP.P1)

# create an analog input channel on pin 1
LDR = AnalogIn(mcp, MCP.P2)
#set up button
button = digitalio.DigitalInOut(board.D26)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

def ConvertTemp(data):

  temp = data - 0.5
  temp = temp /0.01
  return round(temp,2)



#temp runtime
runtime = 0
interval = 10

def cycle():
  global interval
  if interval == 10:
    interval = 5
  elif interval == 5:
    interval = 1
  else:
    interval = 10

def print_time_thread():
  global ADC,LDR,runtime,interval
  thread = threading.Timer(interval, print_time_thread)
  thread.daemon = True  # Daemon threads exit when the program does
  thread.start()
  print((str(runtime)+ "s").ljust(9,' '), 	#runtime
	str(ADC.value).ljust(14,' '), 		#temp adc
	(str(ConvertTemp(ADC.voltage))+"C").ljust(9,' '), 		    #temp C
	LDR.value) 				                #light resistor reading
  runtime += interval

if __name__ == "__main__":
  print("Runtime   Temp Reading   Temp      Light Reading")
  print_time_thread()
  while True:
    if button.value == False:
      time.sleep(0.25)
      cycle()
      
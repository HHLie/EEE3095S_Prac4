
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#for waiting
import time

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


runtime = 0
temp = 0
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

# create an analog input channel on pin 1
chan2 = AnalogIn(mcp, MCP.P2)

#while True:
	#print("Raw ADC Value: ", chan.value)
	#print("ADC Voltage: " + str(chan.voltage) + "V")


while True:
	print("Runtime   Temp Reading   Temp      Light Reading")
	print(str(runtime).ljust(9,' '), 	#runtime
	str(chan.value).ljust(14,' '), 		#temp adc
	(str(temp)+"C").ljust(9,' '), 		#temp C
	chan2.value) 				#light resistor reading
	time.sleep(1)
	runtime+=1

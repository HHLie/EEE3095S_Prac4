# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#placeholder import for now
import time

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

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

def ConvertTemp(data):

  temp = data - 0.5
  temp = temp /0.01
  return temp

t = ConvertTemp(ADC.voltage)
tem = round((ADC.voltage-0.5)/0.01)

print("Raw ADC Value: ", ADC.value)
print("ADC Voltage: " + str(ADC.voltage) + "V")
print("temp: "  + str(tem))

#temp runtime
runtime = 0

#do this

def PrintTable():
  while True:
	  print("Runtime   Temp Reading   Temp      Light Reading")

	  print(str(runtime).ljust(9,' '), 	#runtime
	  str(ADC.value).ljust(14,' '), 		#temp adc
	  (str(t)+"C").ljust(9,' '), 		    #temp C
	  LDR.value) 				                #light resistor reading

    #remove later
	  time.sleep(1)
	  runtime+=1

if __name__ == "__main__":
  PrintTable()
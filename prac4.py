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


#print("Raw ADC Value: ", ADC.value)
#print("ADC Voltage: " + str(ADC.voltage) + "V")

#temp runtime
runtime = 0

class MyThread(threading.Thread):
  def __init__(self):
    self.runtime = 10
    self.lock = threading.RLock()
    super(MyThread, self).__init__()
  
  def set_time(self):
    if self.runtime == 10:
      self.runtime = 5
    elif self.runtime == 5:
      self.runtime = 1
    else:
      self.runtime = 10
  
  def run(self):
    while True:
      print(str(self.runtime).ljust(9,' '), 	#runtime
      str(ADC.value).ljust(14,' '), 		#temp adc
      (str(ConvertTemp(ADC.voltage))+"C").ljust(9,' '), 		    #temp C
      LDR.value) 				                #light resistor reading
      
      #remove later
      time.sleep(self.runtime)



def PrintTable():
  global ADC,LDR,runtime
  while True:
	  print("Runtime   Temp Reading   Temp      Light Reading")

	  print(str(runtime).ljust(9,' '), 	#runtime
	  str(ADC.value).ljust(14,' '), 		#temp adc
	  (str(ConvertTemp(ADC.voltage))+"C").ljust(9,' '), 		    #temp C
	  LDR.value) 				                #light resistor reading
    
    #remove later
	  time.sleep(1)
	  runtime+=1



if __name__ == "__main__":
  print("Runtime   Temp Reading   Temp      Light Reading")
  interval = 10
  blink_thread = MyThread()
  blink_thread.start()
  while True:
    if button.value == False:
      time.sleep(0.25)
      blink_thread.set_time()
      
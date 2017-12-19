import minimalmodbus
import serial
import time


instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600
instrument.debug = True
instrument.serial.bytesize = 8
#instrument.serial.parity = serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout = 1.0
#instrument.mode = minimalmodbus.MODE_RTU


while 1:
	print("Register: ", 17, " ", instrument.read_register(17,functioncode=3))
	#for i in range(10,56):
	#	print("Register: ", i, " ", instrument.read_register(i,functioncode=3))
	#print(instrument.read_register(0x4C, 1))
	#print(instrument.read_register(0x4D, 1))
	print("=============================================")
	time.sleep(1)


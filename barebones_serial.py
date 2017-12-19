import serial
import time
import binascii

s = serial.Serial('/dev/ttyUSB0', 9600)
# Writing to instrument (expecting 7 bytes back): '\x01\x03\x00\x11\x00\x01Ô\x0f' (01 03 00 11 00 01 D4 0F)
byte_message = binascii.unhexlify('010300110001D40F')
s.write(byte_message)
time.sleep(0.2)


print("Response from device: ", s.read(7))

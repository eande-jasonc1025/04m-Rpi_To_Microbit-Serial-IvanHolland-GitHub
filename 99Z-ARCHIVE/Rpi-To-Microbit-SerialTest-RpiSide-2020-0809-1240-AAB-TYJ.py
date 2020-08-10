# Write your code here :-)
import serial

# Open the serial port for sending at speed 115200 bits/second
device = serial.Serial('/dev/ttyACM0', 115200)

# Write string to serial port, and terminate with a line feed character
##jwc y serialString_Tx = "22\n"
serialString_Tx = "Hello Jesus :)\n"

##jwc n device.write("22\n")
device.write(serialString_Tx.encode())
##jwc n device.write(b'\x0101')


# Close serial port
device.close()
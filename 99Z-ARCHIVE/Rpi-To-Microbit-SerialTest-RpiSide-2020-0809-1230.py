import serial

# Open the serial port for sending at speed 115200 bits/second
device = serial.Serial('/dev/ttyACM0', 115200)

# Write string to serial port, and terminate with a line feed character
d = to_bytes("22\n")
device.write(d)

# Close serial port
device.close()
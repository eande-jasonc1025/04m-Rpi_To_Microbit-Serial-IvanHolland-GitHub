# Write your code here :-)
import serial
import tkinter as tk


# Open the serial port for sending at speed 115200 bits/second
device = serial.Serial('/dev/ttyACM0', 115200)

# Write string to serial port, and terminate with a line feed character
##jwc y serialString_Tx = "22\n"
##jwc y serialString_Tx = "Hello Jesus :)\n"
serialString_Tx = ":)\n"


# Declare global variables
counter = None

# This function is called whenever the button is pressed
def count():

    global counter

    # Increment counter by 1
    counter.set(counter.get() + 1)    

    ##jwc n device.write("22\n")
    device.write(serialString_Tx.encode())
    ##jwc n device.write(b'\x0101')    


# This function is called whenever the button is pressed
def count_02():

    global counter

    # Increment counter by 1
    counter.set(0)    
    
    # Close serial port
    device.close()

# Create the main window
root = tk.Tk()
root.title("Counter")

# Tkinter variable for holding a counter
counter = tk.IntVar()
counter.set(0)

# Create widgets (note that command is set to count and not count() )
label_counter = tk.Label(root, width=7, textvariable=counter)
button_counter = tk.Button(root, text="Count", command=count)
button_02_counter = tk.Button(root, text="Count_02", command=count_02)

# Lay out widgets
label_counter.pack()
button_counter.pack()
button_02_counter.pack()

# Run forever!
root.mainloop()


# Write your code here :-)
import serial
import tkinter as tk


# Open the serial port for sending at speed 115200 bits/second
###jwc undo: device = serial.Serial('/dev/ttyACM0', 115200)
microBit_Serial_Obj = serial.Serial('/dev/ttyACM0', 115200)
###jwc debug y cd: microBit_Serial_Obj = serial.Serial('/dev/ttyAMA0', 115200)

# Write string to serial port, and terminate with a line feed character
##jwc y serialString_Tx = "22\n"
##jwc y serialString_Tx = "Hello Jesus :)\n"
##jwc y serialString_Tx = ":)\n"
##jwc ? buffer overload: rpi_Microbit_1CharMsg_Forward_Str = "forward\n"
##jwc ? buffer overload: rpi_Microbit_1CharMsg_Backward_Str = "backward\n"
##jwc ? rpi_Microbit_1CharMsg_Forward_Str = "fo\n"
##jwc ? rpi_Microbit_1CharMsg_Backward_Str = "ba\n"
rpi_Microbit_1CharMsg_Forward_Str = "f\n"
rpi_Microbit_1CharMsg_Backward_Str = "b\n"
rpi_Microbit_1CharMsg_Left_Str = "l\n"
rpi_Microbit_1CharMsg_Right_Str = "r\n"
rpi_Microbit_1CharMsg_Stop_Str = "s\n"
rpi_Microbit_1CharMsg_ForwardLeft_Str = "8\n"
rpi_Microbit_1CharMsg_ForwardRight_Str = "9\n"
rpi_Microbit_1CharMsg_ArmForward_Down_Str = "d\n"
rpi_Microbit_1CharMsg_ArmBackward_Up_Str = "u\n"
rpi_Microbit_1CharMsg_Gear1_Str = "1\n"
rpi_Microbit_1CharMsg_Gear2_Str = "2\n"


# Declare global variables
counter_Int_Obj = None

def sendTx_Foward_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_Forward_Str.encode())
def sendTx_Backward_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_Backward_Str.encode())
def sendTx_Left_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_Left_Str.encode())
def sendTx_Right_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_Right_Str.encode())
def sendTx_ForwardLeft_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_ForwardLeft_Str.encode())
def sendTx_ForwardRight_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_ForwardRight_Str.encode())

def sendTx_ArmForward_Down_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_ArmForward_Down_Str.encode())
def sendTx_ArmBackward_Up_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_ArmBackward_Up_Str.encode())

def sendTx_Gear1_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_Gear1_Str.encode())
def sendTx_Gear2_Fn():
    counter_Int_Obj.set(counter_Int_Obj.get() + 1)    
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_Gear2_Str.encode())

def sendTx_Stop_Fn():
    counter_Int_Obj.set(0)
    microBit_Serial_Obj.write(rpi_Microbit_1CharMsg_Stop_Str.encode())
    # Close serial port
    ##jwc y microBit_Serial_Obj.close()

# Create the main window
windowMain_Obj = tk.Tk()
windowMain_Obj.title("Counter")

# Tkinter variable for holding a counter_Int_Obj
counter_Int_Obj = tk.IntVar()
counter_Int_Obj.set(0)

# Create widgets
# !!! NOTE: Command is set to 'sendTx_Foward_Fn' and not 'sendTx_Foward_Fn()', thus cannot handle arguments
counter_TkLbl = tk.Label(windowMain_Obj, width=7, textvariable=counter_Int_Obj)

button_Forward_TkBtn = tk.Button(windowMain_Obj, text="Forward", command=sendTx_Foward_Fn)
button_Backward_TkBtn = tk.Button(windowMain_Obj, text="Backward", command=sendTx_Backward_Fn)
button_Left_TkBtn = tk.Button(windowMain_Obj, text="Left", command=sendTx_Left_Fn)
button_Right_TkBtn = tk.Button(windowMain_Obj, text="Right", command=sendTx_Right_Fn)
button_ForwardLeft_TkBtn = tk.Button(windowMain_Obj, text="FwdLeft", command=sendTx_ForwardLeft_Fn)
button_ForwardRight_TkBtn = tk.Button(windowMain_Obj, text="FwdRight", command=sendTx_ForwardRight_Fn)

button_ArmForward_Down_TkBtn = tk.Button(windowMain_Obj, text="ArmForward_Down", command=sendTx_ArmForward_Down_Fn)
button_ArmBackward_Up_TkBtn = tk.Button(windowMain_Obj, text="ArmBackward_Up", command=sendTx_ArmBackward_Up_Fn)

button_Gear1_TkBtn = tk.Button(windowMain_Obj, text="Gear1", command=sendTx_Gear1_Fn)
button_Gear2_TkBtn = tk.Button(windowMain_Obj, text="Gear2", command=sendTx_Gear2_Fn)

button_Stop_TkBtn = tk.Button(windowMain_Obj, text="Stop", command=sendTx_Stop_Fn)

# Lay out widgets
counter_TkLbl.pack()
button_Forward_TkBtn.pack()
button_Backward_TkBtn.pack()
button_Left_TkBtn.pack()
button_Right_TkBtn.pack()
button_ForwardLeft_TkBtn.pack()
button_ForwardRight_TkBtn.pack()

button_ArmForward_Down_TkBtn.pack()
button_ArmBackward_Up_TkBtn.pack()

button_Gear1_TkBtn.pack()
button_Gear2_TkBtn.pack()

button_Stop_TkBtn.pack()

# Run forever!
windowMain_Obj.mainloop()
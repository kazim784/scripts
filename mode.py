import serial

# Open the serial port
ser = serial.Serial('/dev/serial0', 1500000, timeout=1)

# Send the command to change to GUIDED mode
ser.write(b"mode GUIDED\n")
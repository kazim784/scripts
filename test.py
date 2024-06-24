import serial
import time

# Open the serial port
ser = serial.Serial('/dev/serial0', 1500000, timeout=1)

# Wait for the vehicle to respond
while True:
    ser.write(b"sysid 1\n")  # Send a MAVLink message to request the system ID
    response = ser.readline()
    if response:
        print("Received response:", response)
        break
    time.sleep(0.1)

# Send a heartbeat message to the vehicle
ser.write(b"heartbeat 1 1 1 1\n")

# Wait for the vehicle to respond with a heartbeat message
while True:
    response = ser.readline()
    if response:
        print("Received heartbeat response:", response)
        break
    time.sleep(0.1)

print("Connected to vehicle!")
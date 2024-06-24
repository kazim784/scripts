import serial
import time

try:
    # Open the serial port
    ser = serial.Serial('/dev/serial0', 1500000, timeout=1)
    print("Serial port opened successfully")
except serial.SerialException as e:
    print("Error opening serial port:", e)
    exit(1)

while True:
    try:
        # Send a MAVLink message to request the system ID
        ser.write(b"sysid 1\n")
        print("Sent sysid message")
        response = ser.readline()
        if response:
            print("Received response:", response)
            break
        time.sleep(0.1)
    except serial.SerialException as e:
        print("Error reading from serial port:", e)
        time.sleep(1)

try:
    # Send a heartbeat message to the vehicle
    ser.write(b"heartbeat 1 1 1 1\n")
    print("Sent heartbeat message")
except serial.SerialException as e:
    print("Error writing to serial port:", e)

while True:
    try:
        response = ser.readline()
        if response:
            print("Received heartbeat response:", response)
            break
        time.sleep(0.1)
    except serial.SerialException as e:
        print("Error reading from serial port:", e)
        time.sleep(1)

print("Connected to vehicle!")
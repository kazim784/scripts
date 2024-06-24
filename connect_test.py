##########DEPENDENCIES#############

from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import exceptions
import math
import argparse


#########FUNCTIONS#################

#connection_string='/dev/ttyTHS1'
#baud=57600

def connectMyCopter():
    print("Connecting to the copter...")
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect

    print("Connecting to:", connection_string)
    vehicle = connect(connection_string, baud=57600, wait_ready=True)

    print("Connected to the copter!")
    return vehicle

def arm():
    print("Arming the copter...")
    while vehicle.is_armable != True:
        print("Waiting for vehicle to become armable.")
        time.sleep(1)
    print("Vehicle is now armable")

    vehicle.mode = VehicleMode("GUIDED")

    while vehicle.mode != 'GUIDED':
        print("Waiting for drone to enter GUIDED flight mode")
        time.sleep(1)
    print("Vehicle now in GUIDED MODE. Have fun!!")

    vehicle.armed = True
    while vehicle.armed == False:
        print("Waiting for vehicle to become armed.")
        time.sleep(1)
    print("Vehicle is now armed.")
    return None

##########MAIN EXECUTABLE###########

print("Script started...")
vehicle = connectMyCopter()

print("Getting autopilot version...")
vehicle.wait_ready('autopilot_version')
print('Autopilot version: %s' % vehicle.version)

print("Arming the copter...")
arm()
print("Script finished!")
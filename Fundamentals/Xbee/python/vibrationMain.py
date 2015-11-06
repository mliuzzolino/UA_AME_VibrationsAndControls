"""
    Authors: Michael Iuzzolino
    Organization: University of Arizona
    Date: September - December 2015

Notes:
Possible mechanism for breaking out of data collect...

            try:   
                # Stuff
            except KeyboardInterrupt:
                print('exiting from keyboard interrupt!')


Good references on 3D plotting:

    1)  http://stackoverflow.com/questions/16037494/python-code-is-it-comma-operator

    2)  https://fossies.org/dox/matplotlib-1.4.3/art3d_8py_source.html

"""


import sys, serial, glob, time, argparse
import modules.handShake as hs
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from collections import deque



                    


def collect_data(serial_socket):
    

    # Handshake with device for mode change
    python_send = 0
    arduino_success = 126
    arduino_fail = 128

    hs.hand_shake(serial_socket, python_send, arduino_success, arduino_fail)
    # HANDSHAKE complete





    print("Plotting data now...")

    while True:
        while serial_socket.inWaiting() > 0:
            try:
                tempValue = ord(serial_socket.read(1)) * 0.004882814
                degreesC = (tempValue - 0.5) * 100.0
                print(degreesC)
            except SerialException:
                print("Fail")            


            



def print_menu(delay=0):
    
    print("\n")
    time.sleep(delay)
    print("\t=======================")
    time.sleep(delay)
    print("\t|        Menu         |")
    time.sleep(delay)
    print("\t|---------------------|")
    time.sleep(delay)
    print("\t|  [c]ollect  data    |")
    time.sleep(delay)
    print("\t|                     |")
    time.sleep(delay)
    print("\t=======================")
    print("\n")



def main():

    # Initial With Device Handshake
    serial_socket = hs.choose_serial_ports()

    # Welcome message
    print("\n\nWelcome to the vibrations program!")

    # Print Menu
    print_menu()
    
    while True:
       
        # Get mode from user
        mode = raw_input("> ")

        # Mode 'c': Collect Data
        if (mode == 'c'):
            print("\tEntering collect data mode...")
            collect_data(serial_socket)
        else:
            print("\tIncorrect entry. Try again!")
            time.sleep(0.5)
            print_menu(0.1)
    


if __name__ == "__main__":
    main()




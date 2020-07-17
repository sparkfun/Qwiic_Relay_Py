#!/usr/bin/env python
#-----------------------------------------------------------------------------
# qwiic_relay_ex1.py
#
# Example that shows the basics of using the quad and dual relays.
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, July 2020
# 
# This python library supports the SparkFun Electronics qwiic 
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatible) single
# board computers. 
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2020 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
# Example 1
#

from __future__ import print_function
import qwiic_relay
import time
import sys


QUAD_RELAY = 0x6D
SINGLE_RELAY = 0x18
QUAD_SOLID_STATE_RELAY = 0x08

#Be sure to initialize your relay with the proper address.
myRelays = qwiic_relay.QwiicRelay(QUAD_SOLID_STATE_RELAY)

def runExample():

    print("\nSparkFun Qwiic Relay Example 1\n")

    if myRelays.begin() == False:
        print("The Qwiic Relay isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    #Turn on relays one and three
    myRelays.set_relay_on(1)
    myRelays.set_relay_on(3)
    time.sleep(1)
    
    #Print the status of all relays
    for relayNum in range(4):
        current_status = None
        if myRelays.get_relay_state(relayNum) is True:
            current_status = "On"
        else:
            current_status = "Off"
        print("Status 1: " + current_status + "\n")
    
    #Turn off 1 and 3, turn on 2 and 4
    myRelays.set_relay_off(1)
    myRelays.set_relay_on(2)
    myRelays.set_relay_off(3)
    myRelays.set_relay_on(4)
    time.sleep(1)
    

    #Turn all relays on, then turn them all off
    myRelays.set_all_relays_on()
    time.sleep(1)
    
    myRelays.set_all_relays_off()
    


if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
#!/usr/bin/env python
#-----------------------------------------------------------------------------
# top_phat_button_ex2.py
#
# Example that shows how to set and get the slow PWM value
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, April 2020
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
# Copyright (c) 2019 SparkFun Electronics
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
# Example 2
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

    print("\nSparkFun Qwiic Relay Example 2\n")

    if myRelays.begin() == False:
        print("The Qwiic Relay isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    #Note that our range is 0-120 for setting a PWM value as there are only 120 times where the zero crossing relay can switch in one second

    myRelays.set_slow_pwm(1, 30) #25% duty cycle
    myRelays.set_slow_pwm(2, 60) #50% duty cycle
    myRelays.set_slow_pwm(3, 90) #75% duty cycle
    myRelays.set_slow_pwm(4, 120) #100% duty cycle

    #Print out our PWM values 
    for relayNum in range(1, 5):
        pwmValue = myRelays.get_slow_pwm(relayNum)
        print("PWM Value for relay " + str(relayNum) + ": " + str(pwmValue))
    #Let the slow PWM run for a while
    time.sleep(15)
    
    
    #Set all relays off 
    myRelays.set_slow_pwm(1, 0)
    myRelays.set_slow_pwm(2, 0)
    myRelays.set_slow_pwm(3, 0)
    myRelays.set_slow_pwm(4, 0)

if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
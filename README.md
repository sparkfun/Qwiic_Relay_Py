Qwiic_Relay_Py
==================
<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-relay/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun-qwiic-relay.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Relay_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_Relay_Py.svg" /></a>
	<a href="https://sparkfun-qwiic-relay.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/sparkfun-qwiic-relay/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Relay_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>
	
</p>

<img src="https://cdn.sparkfun.com/assets/parts/1/5/7/5/4/16833-SparkFun_Qwiic_Quad_Solid_State_Relay_Kit-01.jpg"  align="right" width=300 alt="SparkFun Qwiic Solid State Relay">

Python module for the Qwiic Relays, Listed below
* [SparkFun Qwiic Single Relay](https://www.sparkfun.com/products/15093)
* [SparkFun Qwiic Quad Relay](https://www.sparkfun.com/products/15102)
* [SparkFun Qwiic Dual Solid State Relay](https://www.sparkfun.com/products/16810)
* [SparkFun Qwiic Quad Solid State Relay](https://www.sparkfun.com/products/16796)

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

## Contents

* [Supported Platforms](#supported-platforms)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Supported Platforms
--------------------
The Qwiic Relay Python package current supports the following platforms:
* [Raspberry Pi](https://www.sparkfun.com/search/results?term=raspberry+pi)

Dependencies 
---------------
This driver package depends on the qwiic I2C driver: 
[Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)

Documentation
-------------
The SparkFun Qwiic Relay module documentation is hosted at [ReadTheDocs](https://sparkfun-qwiic-relay.readthedocs.io/en/latest/?)

Installation
-------------

### PyPi Installation
This repository is hosted on PyPi as the [sparkfun-qwiic-relay](https://pypi.org/project/sparkfun-qwiic-relay/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-relay
```
For the current user:

```sh
pip install sparkfun-qwiic-relay
```

### Local Installation
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun_qwiic_relay-<version>.tar.gz
  
```
Example Use
 ---------------
See the examples directory for more detailed use examples.

```python
from __future__ import print_function
import qwiic_relay
import time
import sys

myRelays = qwiic_relay.QwiicRelay()

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
```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>

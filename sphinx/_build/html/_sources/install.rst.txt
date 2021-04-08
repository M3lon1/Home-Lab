============
Installation
============
This is an installation guide for the PsyMex-2 project on a Raspberry Pi 4B

******************
Required libraries
******************
In order to install PsyMex-2 you need to install some pyqt5 libraries as well as smbus2

On the command line:

*sudo apt-get install python3-pyqt5*

*sudo apt-get install python3-pyqtgraph*

*sudo apt-get install python3-pyqt5.qtsvg*

*pip3 install smbus2*

******************
Activate GPIO Pins
******************
To activate the GPIO Pins got to:

*Menu > Settings > Raspberry-Pi Configuration > Interface*

and activate *SPI* and *I2C*
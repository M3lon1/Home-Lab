=========
Structure
=========

The project is made up of the following python files

* SensorExample.py
* PsyMexHub.py
* PilotStudie.py
* ScreenSensorGSR.py
* ScreenSensorHR.py
* ScreenInstructions.py
* ScreenInstructions2.py
* ScreenBaseline.py
* ScreenBaseline2.py
* ScreenTask11.py
* ScreenTask12.py
* ScreenTask21.py
* ScreenTask22.py
* ScreenTask31.py
* ScreenTask32.py
* ScreenEnd.py
* grove/adc.py
* grove/grove_gsr_sensor.py
* grove/i2c.py
* pulse/MCP3008.py
* pulse/pulsesensor.py

****************
SensorExample.py
****************
This file contains a simple example on how to start/stop and retrieve data from the sensors.
This can be used in any python script. It is also possible to use the sensors with a QTimer from PyQt5. 
An example can be found in the ScreenBaseline2.py file. Look at the start_measurement and timer function in the file.

****************
PsyMexHub.py
****************
This file builds the hub window built with PyQt5. The layout is build with several nested QVBoxLayout/QHBoxLayout.
To show the different views in the hub, the layouts are altered, no new windows are drawn.

**************
PilotStudie.py
**************
This file is the entry point for the pilot studie. It shows the first screen of it where you can enter participants data.

******************
ScreenSensorGSR.py
******************
This file shows the screen for setting up the GSR sensor and testing it with a live plot.

*****************
ScreenSensorHR.py
*****************
This file shows the screen for setting up the heart rate sensor and testing it with a live plot.

*********************
ScreenInstructions(2)
*********************
Those files show text that explains the procedure of the studie.

********************
ScreenBaseline.py(2)
********************
The first file shows text that explains briefly the baseline measurement.
The second file performs the measurement. The sensors run in the background and the result is saved in a csv file  in the results/ folder.
The screen of the second file shows a cross to look at.

*******************
ScreenTask11(12).py
*******************
Those files show the cognitive task. The last digit shows the difficulty of the task, where 1 is easy 2 is hard. 
This holds for all the ScreenTask files. In this task you eighter have to sum up the number 3 or subtract 17 starting from 7561.

*******************
ScreenTask21(22).py
*******************
Those files show the motion task. In this task you eighter have to open and close your hand repeatedly with or without resistance.

*******************
ScreenTask31(32).py
*******************
Those files show the affective task. In this task you eighter have to look at a neutral or negative picture.

************
ScreenEnd.py
************
This file marks the end of the study. It shows a thank you screen.

************
grove/adc.py
************
This file controlls the I2C ADC attatched to the grove gsr sensor.
The code was taken from `the seeedstudio homepage <https://wiki.seeedstudio.com/Grove-GSR_Sensor/>`_

*************************
grove/grove_gsr_sensor.py
*************************
This file controlls the gsr sensor. It was taken from `the seeedstudio homepage <https://wiki.seeedstudio.com/Grove-GSR_Sensor/>`_.
The file was modified to hold a list of values with their timestamps and starting/stopping the sensor in a separate thread.

************
grove/i2c.py
************
This file is used to connect the grove sensor to the pi
it was taken from `the seeedstudio homepage <https://wiki.seeedstudio.com/Grove-GSR_Sensor/>`_

****************
pulse/MCP3008.py
****************
This file controlls the adc used for the pulse sensor. The code was taken from `this tutorial <https://tutorials-raspberrypi.de/raspberry-pi-puls-herzfrequenz-messen/>`_

********************
pulse/pulsesensor.py
********************
This file controlls the pulse sensor. The code was taken from `this tutorial <https://tutorials-raspberrypi.de/raspberry-pi-puls-herzfrequenz-messen/>`_.
The code was extended to hold the values and timestamp in a list. Functions to compute the RMSSD and SDNN are added.


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
* AnalysisPlot.py
* NexusToCSV.py

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

***************
AnalysisPlot.py
***************
This file is used to plot Nexus and PsyMex data together and calculate their korrelation, variance, and mean.
The plot just works for GSR values right now. In order to use the Nexus data you have to get them in the right format via the NexusToCSV.py file.
To fit the Nexus and PsyMex starting and end point of the measurement you can set them during initialization of the class AnalysisPlot().
The AnalysisPlot() class takes 6 positional arguments for initialization.
1. path to psymex csv file.
2. path to prepared nexus csv file.
3. nexus start time in seconds.
4. nexus end time in seconds.
5. psymex start time in seconds.
6. psymex end time in seconds.

If you want to plot everything from beginning to end you can set start = 0 and end = math.inf.

In an early version there where two separate plots for psymex and nexus data. Code is still there you just have to uncomment it if you want to use separate plots.
If you want to use it, there are two lines that you have to uncomment which are obviously highlighted.
1. Add the plot widget to the overall layout.
2. Plot the data to their specific plot.

*************
NexusToCSV.py
*************
This file is used to convert the Nexus file to a file that can be used with psymex AnalysisPlot.py file.
Therefore export the Nexus session with the extended option "Include Time (as sample interval) / Zeit einschließen (als Sample-Intervalle)"
Set the path variable to point to the exported nexus file. Set the output variable to the path where you want to store the output.
The output file contains of several lines containing the time stamp and the gsr value, an example line looks like this. 

"1.849","1"

The first number is the value and the second number is the time stamp.
Note that this file currently just converts Nexus GSR output.


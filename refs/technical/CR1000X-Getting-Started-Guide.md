Getting Started Guide
LoggerNet/PC400 Version

CR1000X/CR1000Xe

Measurement and Control Datalogger

Revision: 09/2024
Copyright © 2000 – 2024
Campbell Scientific, Inc.

Table of Contents

1. Getting started

2. USB communications

3. Testing communications with EZSetup

4. Making the software connection

5. Creating a Short Cut data logger program

6. Sending a program to the data logger

7. Working with data

7.1 Default data tables
7.2 Collecting data

7.2.1 Collecting data using LoggerNet
7.2.2 Collecting data using PC400

7.3 Viewing historic data

1

2

4

6

8

12

14

14
15
15
15
16

Table of Contents - i

1. Getting started

Getting started provides a cursory view of data acquisition and walks you through a procedure to
set up a simple system. You may not find it necessary to progress beyond this. However, should
you want to dig deeper into the complexity of the data logger functions or quickly look for
details, extensive information is available in the full CR1000X/CR1000Xe manual.

This exercise guides you through the following steps:

 l Connecting the data logger to a computer
 l Attaching a sensor to the data logger
 l Creating a program for the data logger to measure the sensor
 l Making a simple measurement
 l Storing measurement data on the data logger
 l Collecting data from the data logger with a computer
 l Viewing real-time and historical data with a computer

In addition to your data logger, the following items are used in this exercise (many are shipped
with your data logger and all are available on www.campbellsci.com

):

 l Type T thermocouple, 4 to 5 inches long; one is shipped with the data logger
 l Computer with a USB port
 l USB cable
 l USB-C cable (CR1000Xe only)
 l Data logger support software such as LoggerNet or PC400 installed on your computer

Additional Campbell Scientific publications are available online at www.campbellsci.com
Video tutorials  are available at www.campbellsci.com/videos
of the data logger requires a peripheral hardware device, more information is available in the
manual written for that device.

. Generally, if a particular feature

.

1. Getting started     1

2. USB communications

Setting up a USB connection is a good way to begin communicating with your data logger.
Because this connection does not require configuration (like an IP address), you need only set up
the communications between your computer and the data logger. Use the following instructions
or watch the Quickstart videos at https://www.campbellsci.com/videos

.

TIP:
You will physically connect your data logger to your computer in step 6.

Follow these steps to get started. These settings can be revisited using the data logger support
software Edit Datalogger Setup option

.

 1.  Using data logger support software, launch the EZSetup Wizard.

NOTE:
New software installations automatically open the EZSetup Wizard the first time they
run.

 l LoggerNet users, click Setup , select the View menu and ensure you are in the EZ

(Simplified) view, then click Add Datalogger

.

 l PC400 users, click Add Datalogger

.

 2.  Click Next.

 3.  Select your data logger from the list. In the Datalogger Name field, type a meaningful

name for your data logger (for example, a site identifier or project name), and click Next.

 4.  Select the Direct Connect connection type and click Next.

 5.  If this is the first time connecting this computer to a CR1000X/CR1000Xe via USB, click Install

USB Driver, select your data logger, click Install, and follow the prompts to install the
USB driver.

 6.  Plug the data logger into your computer using a USB  cable. The USB connection supplies
5 V power as well as a communications link, which is adequate for setup. A 12 V battery will
be needed for field deployment. If using RS-232, external power must be provided to the
data logger, and a CPI/RS-232 RJ45 to DB9 cable is required to connect to the computer.

2. USB communications     2

NOTE:
The Power LED on the data logger indicates the program and power states. Because
the data logger ships with a program set to run on power-up, the Power LED flashes
three times every 10 seconds when powered over USB. When powered with a 12 V
battery, it flashes once every 10 seconds. When no program is running, the LED is
always on.

 7.  From the COM Port list, select the COM port used for your data logger. It will appear as

CR1000X/CR1000Xe (COM number).

 8.  USB connections do not typically require a COM Port Communication Delay; this type of

delay allows time for hardware devices to "wake up" and negotiate a communications link.
Accept the default value of 00 seconds and click Next.

 9.  You must match the PakBus address hardware settings of your data logger. A USB

connection does not require a baud rate selection, keep the default.  The default PakBus
address is 1.

 10.  Set an Extra Response Time if you have a difficult or marginal connection and you want the

data logger support software to wait a certain amount of time before returning a
communications failure error. Accept the default value of 00 seconds.

 11.  Set a Max Time On-Line to limit the amount of time the data logger remains connected.

When the data logger is connected, communications with it are terminated when this time
limit is exceeded. A value of 0 in this field indicates that there is no time limit for
maintaining a connection to the data logger.

 12.  Leave the Neighbor PakBus Address as the default of 0.

 13.  Click Next.

 14.  By default, the data logger does not use a security code. Therefore, the Security Code can

be left at 0. If the code has been changed in the data logger, enter the new code.

The PakBus Encryption Key can be left blank for direct USB connections.

 15.  Click Next.

 16.  Review the Setup Summary. If you need to make changes, click Previous to return to a

previous window and change the settings.

 17.  Setup is now complete. The EZSetup Wizard allows you to Finish, or you may click Next to

test communications, set the data logger clock, and send a program to the data logger.

2. USB communications     3

3. Testing communications with
EZSetup

 1.  Advance to, or select,  the Communication Test step in EZ Setup. See USB communications

(p. 2) for more information.

 2.  Ensure the data logger is physically connected to the computer, select Yes to test

communications, then click Next to initiate the test.

 3.  With a successful connection, the Connection Time  with the data logger is displayed in the

lower-left corner of the wizard. Click Next.

 4.   The Datalogger Clock window displays the time for both the data logger and the computer

(server).

 l The Adjusted Server Date/Time displays the current reading of the clock for the

computer running your data logger support software. If the Datalogger Date/Time
and Adjusted Server Date/Time do not match,  click Set Datalogger Clock to set the
data logger clock to the computer clock.

 l Optionally, specify a positive or negative Time Zone Offset to apply when setting the
data logger clock. This offset allows you to set the clock for a data logger that is in a
different time zone than the computer (or to accommodate for changes in daylight
saving time).

 5.  Click Next.

3. Testing communications with EZSetup     4

 6.  The data logger ships with a default GettingStarted program. If the data logger does not
have a program, you can choose to send one by clicking Select and Send Program.  Click
Next.

 7.  LoggerNet only - Use the following instructions or watch the Scheduled/Automatic Data

Collection video

:

 l The Datalogger Table Output Files window displays the data tables available to be

collected from the data logger and the output file name. By default, all data tables set
up in the data logger program will be included for collection.  Make note of the
Output File Name and location. Click Next.

 l Check Scheduled Collection Enabled to have LoggerNet automatically collect data
from the data logger on the Collection Interval entered. When the Base Date and
Time are in the past, scheduled collection will begin immediately after finishing the
EZSetup wizard. Do not set up a scheduled collection during this tutorial. Click Next.

 8.  Click Finish, or you may click Next to test communications, set the data logger clock, and

send a program to the data logger.

3. Testing communications with EZSetup     5

4. Making the software
connection

Once you have configured your hardware connection (see USB communications [p. 2]), your data
logger and computer can communicate. Use the Connect screen to send a program, set the
clock, view real-time data, and manually collect data.

LoggerNet users, select the Main category and Connect
the data logger from the Stations list, then click Connect
view in the Table Monitor.

 on the LoggerNet toolbar, then select
. Once connected, select a table to

PC400 users, click Connect
values from the Public table are displayed. To view data from other tables, click Add
table or field from the list, then drag it into a cell on the Monitor Data tab.

, then Monitor Data. When this tab is first opened for a data logger,

, select a

For more information, see Working with data (p. 14).

4. Making the software connection     6

NOTE:
When powered only by USB, the battery voltage is reported as 0.00. This is to remind you that
a 12 V battery is needed for field deployment.

See Collecting data (p. 15) for more information on copying stored data from the data logger to
the computer.

To disconnect, click Disconnect

.

For more information,  see the Connect Window Tutorial

.

4. Making the software connection     7

5. Creating a Short Cut data
logger program

You must provide a program for the data logger in order for it to make measurements, store
data, or control external devices. There are several ways to write a program. The simplest is to use
the program generator called Short Cut. For more complex programming, CRBasic Editor is used.
The program file may use the extension  .CR1X, .CRB, or .DLD.

Data logger programs are executed on a precise schedule termed the scan interval, based on the
data logger internal clock.

Measurements are first stored in temporary memory called variables in the Public table. Data
stored in variables is usually overwritten each scan. Periodically, generally on a time interval, the
data logger stores data in tables. The data tables are later copied to a computer using your data
logger support software.

Use Short Cut software to generate a program for your data logger. Short Cut is included with
your data logger support software.

This section guides you through programming a CR1000X/CR1000Xe data logger to measure the
voltage of the data logger power supply, the internal temperature of the data logger, and a
thermocouple. With minor changes, these steps can apply to other measurements.             Use the
following instructions or watch the Quickstart part 3 video

:

 1.  Using data logger support software, launch Short Cut.

 l LoggerNet users, click Program then Short Cut

.

 l PC400 users, click Short Cut

.

 2.  Click Create New Program.

 3.  Select CR1000X Series and click Next.

NOTE:
The first time Short Cut is run, a prompt asks for a noise rejection choice. Select 60 Hz
Noise Rejection for North America and areas using 60 Hz ac voltage. Select 50 Hz Noise
Rejection for most of the Eastern Hemisphere and areas that operate at 50 Hz.

A second prompt lists sensor support options. Campbell Scientific, Inc. (US) is usually
the best fit outside of Europe.

5. Creating a Short Cut data logger program     8

To change the noise rejection or sensor support option for future programs, use the
Program menu.

 4.  Lists of Available Sensors and Devices and Selected Measurements Available for Output are
displayed. Battery voltage BattV and internal temperature PTemp_C are selected by
default. During operation, battery and temperature should be recorded at least daily to
assist in monitoring system status.

 5.  Use the Search feature or expand folders to locate your sensor or device. Double-click on a
sensor or measurement in the Available Sensors and Devices list to configure the device (if
needed) and add it to the Selected list. For the example program, expand the Sensors and
Temperature folders and double-click Type T Thermocouple.

 6.  If the sensor or device requires configuration, a window displays with configuration

options. Click Help at the bottom of the window to learn more about any field or option.
For the example program, accept the default options:

 l 1 Type T TC sensor

 l Temp_C as the Temperature label, and set the units to Deg C

 l PTemp_C as the Reference Temperature Measurement

 7.  Click the Wiring tab at the top of the page to see how to wire the sensor to the data logger.
With the power disconnected from the data logger, insert the wires as directed in the
diagram. Ensure you clamp the terminal on the wire, not the colored insulation. Use the
included flat-blade screwdriver to open and close the terminals.

 8.  Click OK.

 9.  Click Next.

 10.  Use the Output Setup options to specify how often to make measurements and how often
outputs are to be stored. Type 1 in the How often should the data logger measure its
sensor(s)? box. Leave the units as Seconds.

 11.  Multiple output intervals can be specified, one for each output table (Table1 and Table2
tabs). For the example program, only one table is needed. Click the Table2 tab and click
Delete Table.

 12.  In the Table Name box, type a name for the table. For example: OneMin.

 13.  Select a Data Output Storage Interval. For example: 1 minute.

 14.  Click Next.

5. Creating a Short Cut data logger program     9

 15.  Select a measurement from the Selected Measurements Available for Output list, then click
an output processing option to add the measurement to the Selected Measurements for
Output list. For the example program, select BattV and click the Minimum button to add it
to the Selected Measurements for Output list. Do not store the exact time that the
minimum occurred. Repeat this procedure for an Average PTemp_C and Average Temp_C.

 16.  Click Finish and give the program a meaningful name such as a site identifier. Click Save.

 17.  If LoggerNet or other data logger support software is running on your computer, and the

data logger is connected to the computer, you can choose to send the program. Generally
it is best to collect data first; so, we recommend sending the program using the instructions
in Sending a program to the data logger (p. 12). Click No, do not send the program to the
data logger.

TIP:
It is good practice to always retrieve data from the data logger before sending a
program; otherwise, data may be lost. See Collecting data (p. 15) for detailed
instruction.

 18.  Make note of the newly generated program location and filename. By default, programs

created with Short Cut are stored in C:\Campbellsci\SCWin\.

 19.  Close Short Cut.

If your data acquisition requirements are simple, you can probably create and maintain a data
logger program exclusively with Short Cut. If your data acquisition needs are more complex, the
files that Short Cut creates are a great source for programming code to start a new program or
add to an existing custom program using CRBasic. See the CRBasic Editor help for detailed
information on program structure, syntax, and each instruction available to the data logger
https://help.campbellsci.com/crbasic/cr1000x/

.

5. Creating a Short Cut data logger program     10

NOTE:
Once a Short Cut generated program has been edited with CRBasic Editor, it can no longer be
modified with Short Cut.

5. Creating a Short Cut data logger program     11

6. Sending a program to the
data logger

TIP:
It is good practice to always retrieve data from the data logger before sending a program;
otherwise, data may be lost. See Collecting data (p. 15) for detailed instruction.

Some methods of sending a program give the option to retain data when possible. Regardless of
the program upload tool used, data will be erased when a new program is sent if any change
occurs to one or more data table structures in the following list:

 l Data table name(s)
 l Data output interval or offset
 l Number of fields per record

 l Number of bytes per field
 l Field type, size, name, or position
 l Number of records in table

            Use the following instructions or watch the Quickstart part 4 video

.

 1.  Connect the data logger to your computer.

 l LoggerNet users, select Main and Connect

 on the LoggerNet toolbar, select the

data logger from the Stations list, then Connect

.

 l PC400 users, select the data logger from the list and click Connect

.

 2.  LoggerNet users, click Send New... (located in the Current Program section on the right side

of the window).

PC400 users, click  Send Program... (located in the Datalogger Program section on the right
side of the window).

 3.  PC400 users, confirm that you would like to proceed and erase all data tables saved on the

data logger. Click Yes.

 4.  Navigate to the program, select it, and click Open. For example: navigate to

C:\Campbellsci\SCWin and select MyTemperature.CR1X. Click Open.

 5.  LoggerNet users, confirm that you would like to proceed and erase all data tables saved on

the data logger. Click Yes.

 6.  The program is sent and compiled.

 7.  Review the Compile Results window for errors, messages and warnings.

6. Sending a program to the data logger     12

 8.  LoggerNet users, click Details, select the Table Fill Times tab.

PC400 user click OK then click Station Status

, select the Table Fill Times tab.

Ensure that the times shown are expected for your application. Click OK.

After sending a program, it is a good idea to monitor the Public table to make sure sensors are
taking good measurements. See Working with data (p. 14) for more information.

6. Sending a program to the data logger     13

7. Working with data

7.1 Default data tables
By default, the data logger includes three tables: Public, Status, and DataTableInfo. Each of these
tables only contains the most recent measurements and information.

 l The Public table is configured by the data logger program, and updated at the scan interval
set within the data logger program. It shows measurement and calculation results as they
are made.

 l The Status table includes information about the health of the data logger and is updated

only when viewed.

 l The DataTableInfo table reports statistics related to data tables. It also only updates when

viewed.

 l User-defined data tables update at the schedule set within the program.

For information on collecting your data, see Collecting data (p. 15).

Use these instructions or follow the Connect Window tutorial

 to monitor real-time data.

LoggerNet users, select the Main category and Connect
the data logger from the Stations list, then click Connect
view in the Table Monitor.

 on the LoggerNet toolbar, then select
. Once connected, select a table to

PC400 users, click Connect
values from the Public table are displayed. To view data from other tables, click Add
table or field from the list, then drag it into a cell on the Monitor Data tab.

, then Monitor Data. When this tab is first opened for a data logger,

, select a

7. Working with data     14

7.2 Collecting data
The data logger writes to data tables  based on intervals and conditions set in the CRBasic
program. After the program has been running for enough time to generate data records, data
may be collected by using data logger support software. During data collection, data is copied to
the computer and still remains on the data logger. Collections may be done manually, or
automatically through scheduled collections set in LoggerNet Setup. Use these instruction or
follow the Collect Data Tutorial

.

7.2.1 Collecting data using LoggerNet

 1.  From the LoggerNet toolbar, click Main and Connect

, select the data logger from the

Stations list, then Connect

.

 2.  Click Collect Now

.

 3.  After the data is collected, the Data Collection Results window displays the tables collected

and where they are stored on the computer.

 4.  Select a data file, then View File to view the data. See Viewing historic data (p. 16).

7.2.2 Collecting data using PC400

 1.  Click Connect

 on the main PC400 window.

 2.  Go to the Collect Data tab.

7. Working with data     15

 3.  By default, all output tables set up in the data logger program are selected for collection.

Typically, the default tables (DataTableInfo, Public, and Status) are not collected.

 4.  Select an option for What to Collect. Either option creates a new file if one does not already

exist.

 l New data from data logger (Append to data files): This is the default, and most often
used option. Collect only the data, in the selected tables, stored since the last data
collection from this instance of PC400 and append this data to the end of the existing
files on the computer.

 l All data from data logger (Overwrite data files): Collects all of the data in the selected

tables and overwrites (or replaces) the existing data files on the computer.

 5.  Click Start Data Collection.

 6.  After the data is collected, the Data Collection Results window displays the tables collected

and where they are stored on the computer.

 7.  Select a data file, then View File to view the data. See Viewing historic data (p. 16).

7.3 Viewing historic data

View Pro
for visualization. Use these instructions or follow the View Data Tutorial

 contains tools for reviewing data in tabular form as well as several graphical layouts

.

Once the data logger has had enough time to store multiple records collect and review the data.

 1.  To view the most recent data, connect the data logger to your computer and collect your

data (see Collecting data (p. 15) for more information).

 2.  Open View Pro:

 l LoggerNet users click Data then View Pro

 on the LoggerNet toolbar.

 l PC400 users click View Data Files via View Pro

.

 3.  Click Open

, navigate to the directory where you saved your tables (the default directory

is C:\Campbellsci\[your data logger software application]). For example: navigate to the
C:\Campbellsci\LoggerNet folder and select OneMin.dat.

 4.  Click Open.

7. Working with data     16

Campbell Scientific Regional Offices

Australia

Location:
Phone:
Email:
Website:

Garbutt, QLD Australia
61.7.4401.7700
info@campbellsci.com.au
www.campbellsci.com.au

France

Location:
Phone:
Email:
Website:

Germany

Montrouge, France
0033.0.1.56.45.15.20
info@campbellsci.fr
www.campbellsci.fr

Spain

Location:
Phone:
Email:
Website:

Thailand

Barcelona, Spain
34.93.2323938
info@campbellsci.es
www.campbellsci.es

Brazil

Location:
Phone:
Email:
Website:

Canada

Location:
Phone:
Email:
Website:

China

Location:
Phone:
Email:
Website:

São Paulo, SP Brazil
11.3732.3399
vendas@campbellsci.com.br
www.campbellsci.com.br

Location:
Phone:
Email:
Website:

Bremen, Germany
49.0.421.460974.0
info@campbellsci.de
www.campbellsci.de

Location:
Phone:
Email:
Website:

Bangkok, Thailand
66.2.719.3399
info@campbellsci.asia
www.campbellsci.asia

Edmonton, AB Canada
780.454.2505
dataloggers@campbellsci.ca
www.campbellsci.ca

Beijing, P. R. China
86.10.6561.0080
info@campbellsci.com.cn
www.campbellsci.com.cn

India

Location:
Phone:
Email:
Website:

Japan

Location:
Phone:
Email:
Website:

New Delhi, DL India
91.11.46500481.482
info@campbellsci.in
www.campbellsci.in

UK

Location:
Phone:
Email:
Website:

Shepshed, Loughborough, UK
44.0.1509.601141
sales@campbellsci.co.uk
www.campbellsci.co.uk

USA

Kawagishi, Toda City, Japan
048.400.5001
jp-info@campbellsci.com
www.campbellsci.co.jp

Location:
Phone:
Email:
Website:

Logan, UT USA
435.227.9120
info@campbellsci.com
www.campbellsci.com

Costa Rica

South Africa

Location:
Phone:
Email:
Website:

San Pedro, Costa Rica
506.2280.1564
info@campbellsci.cc
www.campbellsci.cc

Location:
Phone:
Email:
Website:

Stellenbosch, South Africa
27.21.8809960
sales@campbellsci.co.za
www.campbellsci.co.za


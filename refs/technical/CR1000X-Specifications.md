CR1000X Specifications

Program Execution Period: 1 ms to 1 day

Real-Time Clock:

 l Battery backed while external power is disconnected
 l Resolution: 1 ms
 l Accuracy: ±3 min. per year, optional GPS correction to

±10 µs

Wiring Panel Temperature: Measured using a 10K3A1A
BetaTHERM thermistor, located between the two rows of
analog input terminals.

Physical specifications

Dimensions: 23.8 x 10.1 x 6.2 cm (9.4 x 4.0 x 2.4 in); additional
clearance required for cables and wires.

Weight/Mass: 0.86 kg (1.9 lb)

Case Material: Powder-coated aluminum

Power requirements

Protection: Power inputs are protected against surge, over-
voltage, over-current, and reverse power. IEC 61000-4 Class 4
level.

Power In Terminal:

 l

Input Voltage: 10 to 18 VDC

NOTE: To prevent voltage input issues with sensors
and peripherals, do not use more than 16 V when
powering them through the 12V, SW12-1, SW12-2,
or CS I/O port on the data logger.

 l

Input Current Limit at 12 VDC:

 o 4.35 A at -40 °C
 o 3 A at 20 °C
 o 1.56 A at 85 °C

 l Sustained Input Voltage without Damage: 30 VDC

Vehicle Power Connection: When primary power is pulled from
the vehicle power system, a second power supply OR charge

Electrical specifications are valid over a -40 to +70 °C, non-
condensing environment, unless otherwise specified. Extended
electrical specifications (noted as XT in specifications) are valid
over a -55 to +85 °C non-condensing environment.
Recalibration is recommended every three years. Critical
specifications and system configuration should be confirmed
with Campbell Scientific before purchase.

System specifications

Physical specifications

Power requirements

Power output specifications

Analog measurement specifications

Pulse measurement specifications

Digital input/output specifications

Communications specifications

Standards compliance specifications

Warranty

Terminal functions

System specifications

1

1

1

2

2

4

4

5

5

6

7

Processor: Renesas RX63N (32-bit with hardware FPU, running
at 100 MHz)

Memory:

 l Total onboard: 128 MB of flash + 4 MB battery-backed

SRAM

 o Data storage: 4 MB SRAM + 72 MB flash

(extended data storage automatically used for
auto-allocated Data Tables not being written to
a card)

 o CPU drive: 30 MB flash
 o OS load: 8 MB flash
 o Settings: 1 MB flash
 o Reserved (not accessible): 10 MB flash
 l Data storage expansion: Removable microSD flash

memory, up to 16 GB

Revision: 05/2025
Copyright © 2017 – 2025
Campbell Scientific, Inc.

regulator may be required to overcome the voltage drop at
vehicle start-up.

USB Power: Functions that will be active with USB 5 VDC
applied include sending programs, adjusting data logger
settings, and making some measurements. If USB is the only
power source, then the CS I/O port and the 5V, 12V, and SW12
terminals will not be operational.

Internal Lithium Battery: AA, 2.4 Ah, 3.6 VDC (Tadiran TL
5903/S) for battery-backed SRAM and clock. 3-year life with no
external power source.

Average Current Drain:

Assumes 12 VDC on POWER IN terminals.

Idle: <1 mA

 l
 l Active 1 Hz Scan: 1 mA
 l Active 20 Hz Scan: 55 mA
 l Serial (RS-232/RS-485): Active + 25 mA
 l Ethernet Power Requirements:

 o Ethernet 1 Minute: Active + 1 mA
 o Ethernet Idle: Active + 4 mA
 o Ethernet Link: Active + 47 mA

Power output specifications

System power out limits (when powered with
12 VDC)

Temperature (°C) Current limit1 (A)

–40°

20°

70°

85°

4.53

3.00

1.83

1.56

1 Limited by self-resetting thermal fuse

12 V and SW12 V power output terminals

12V, SW12-1, and SW12-2: Provide unregulated 12 VDC power
with voltage equal to the Power Input supply voltage. These
are disabled when operating on USB power only.

SW12 current limits

Temperature (°C) Current limit 1 (mA)

–40°

0°

20°

50°

70°

80°

1310

1004

900

690

550

470

1 Thermal fuse hold current.

5 V fixed output

5V: One regulated 5 V output. Supply is shared between the 5V
terminal and CS I/O DB9 5 V output.

 l Voltage Output: Regulated 5 V output (±5%)
 l Current Limit: 230 mA

C as power output
 l C Terminals:

 o Output Resistance (Ro): 150 Ω
 o 5 V Logic Level Drive Capacity: 10 mA @ 3.5 VDC
 o 3.3 V Logic Level Drive Capacity: 10 mA @

1.8 VDC

CS I/O pin 1

5 V Logic Level Max Current: 200 mA

Voltage excitation

VX: Four independently configurable voltage terminals (VX1-
VX4).  When providing voltage excitation, a single 16-bit DAC
shared by all VX outputs produces a user-specified voltage
during measurement only.VX terminals can also be used to
supply a selectable, switched, regulated 3.3 or 5 VDC power
source to power digital sensors and toggle control lines.

Range Resolution Accuracy

Voltage
Excitation

±4 V

 0.06 mV

±(0.1% of
setting + 2
mV)

Maximum
source/sink
current1

±40 mA

Switched,
Regulated

+3.3  or
5 V

3.3 or 5 V

±5%

50 mA

1 Exceeding current limits causes voltage output to become
unstable. Voltage should stabilize when current is reduced to within
stated limits.

Analog measurement specifications

16 single-ended (SE) or 8 differential (DIFF) terminals
individually configurable for voltage, thermocouple, current
loop, ratiometric, and period average measurements, using a
24-bit ADC. One channel at a time is measured.

Voltage measurements

Terminals:

 l Differential Configuration: DIFF 1H/1L – 8H/8L
 l Single-Ended Configuration: SE1 – SE16

Input Resistance: 20 GΩ typical

Input Voltage Limits: ±5 V

Sustained Input Voltage without Damage: ±20 VDC

DC Common Mode Rejection:

 l >120 dB with input reversal
 l ≥ 86 dB without input reversal

CR1000X Specifications | May 2, 2025

2

Normal Mode Rejection: > 70 dB @ 60 Hz

Input Current @ 25 °C: ±1 nA typical

Filter First Notch Frequency (fN1) Range: 0.5 Hz to 31.25 kHz
(user specified)

Analog Range and Resolution:

Differential
with input
reversal

Single-ended or
differential
without input reversal

Example fN11
(Hz)

Time2 (ms)

Time2 (ms)

15000

60

50

5

2.04

35.24

41.9

401.9

1 Notch frequency (1/integration time).

2 Default settling time of 500 µs used.

1.02

17.62

20.95

200.95

Resistance measurement specifications

The data logger makes ratiometric-resistance measurements
for four- and six-wire full-bridge circuits and two-, three-, and
four-wire half-bridge circuits using voltage excitation.
Excitation polarity reversal is available to minimize dc error.

Accuracy:

Assumes input reversal for differential measurements
RevDiff and excitation reversal RevExfor excitation voltage
<1000 mV. Does not include bridge resistor errors or sensor
and measurement noise.

 l 0 to 40 °C: ±(0.01% of voltage measurement + offset)
 l –40 to 70 °C: ±(0.015% of voltage measurement +

offset)

 l –55 to 85 °C (XT): ±(0.02% of voltage measurement +

offset)

Differential
with input
reversal

Single-ended
and differential
without input
reversal

Notch
frequency
(fN1) (Hz)

15000

50/603

5

Range1
(mV)

RMS
(µV)

Bits2

RMS
(µV)

Bits2

±5000
±1000
±200

±5000
±1000
±200

±5000
±1000
±200

8.2

1.9

0.75

0.6

0.14

0.05

0.18

0.04

0.02

20

20

19

24

23
22

25

25

24

11.8

2.6

1.0

0.88

0.2

0.08

0.28

0.07

0.03

19

19

18

23

23

22

25

24

23

1 Range overhead of ~5% on all ranges guarantees that full-scale
values will not cause over range

2 Typical effective resolution (ER) in bits; computed from ratio of full-
scale range to RMS resolution.

3 50/60 corresponds to rejection of 50 and 60 Hz ac power mains
noise.

Accuracy (does not include sensor or measurement noise):
 l 0 to 40 °C: ±(0.04% of measurement + offset)
 l –40 to 70 °C: ±(0.06% of measurement + offset)

Voltage Measurement Accuracy Offsets:

Typical offset (µV RMS)

Differential
with input
reversal

Single-ended or
differential
without input reversal

±0.5

±0.25

±0.15

±2

±1

±0.5

Range
(mV)

±5000

±1000

±200

Measurement Settling Time: 20 µs to 600 ms; 500 µs default

Multiplexed Measurement Time:

Measurement Time =

Setup Time + ((Settling Time + 1/fN1) × M × Repetitions)

Where:

M = 1 (default)
M = 2 if reverse differential or measurement offset is used
Setup Time = 150 µs

CR1000X Specifications | May 2, 2025

3

Period-averaging measurement specifications

Accuracy: ±(0.02% of reading + 1/scan)

Terminals: SE1-SE16

Accuracy: ±(0.01% of measurement + resolution), where
resolution is 0.13 µs divided by the number of cycles to be
measured

Ranges:

 l Minimum signal centered around specified period

average threshold.

 l Maximum signal centered around data logger ground.
 l Maximum frequency = 1/(2 * [minimum pulse width])

for 50% duty cycle signals

Gain
code
op-
tion

0

1

2

3

Volt-
age
gain

1

2.5

12.5

64

Min-
imum
peak to
peak
signal
(mV)

Max-
imum
peak to
peak
signal
(V)

Min-
imum
pulse
width
(µs)

Max-
imum
fre-
quency
(kHz)

500

50

10

2

10

2

2

2

2.5

10

62

100

200

50

8

5

Current-loop measurement specifications

The data logger makes current-loop measurements by
measuring across a current-sense resistor associated with the
RS-485 resistive ground terminal.

Terminals: RG1 and RG2

Maximum Input Voltage: ±16 V

Resistance to Ground: 101 Ω

Current Measurement Shunt Resistance: 10 Ω

Maximum Current Measurement Range: ±80 mA

Absolute Maximum Current: ±160 mA

Resolution: ≤ 20 nA

Accuracy: ±(0.1% of reading + 100 nA) @ -40 to 70 °C

Pulse measurement specifications

Terminals individually configurable for switch closure, high-
frequency pulse, or low-level AC measurements. Each terminal
has its own independent 24-bit counter.

NOTE:
Conflicts can occur when a control port pair is used for
different instructions (TimerInput(), PulseCount(),
SDI12Recorder(), WaitDigTrig()). For example, if
C1 is used for SDI12Recorder(), C2 cannot be used for
TimerInput(), PulseCount(), or WaitDigTrig().

Sustained Input Voltage without Damage: ±20 VDC
Maximum Counts Per Scan: 224

Input Resistance: 5 kΩ

Low-level AC input

Terminals: P1-P2

Minimum Pull-Down Resistance: 10 kΩ to ground

DC-offset rejection:  Internal AC coupling eliminates DC-offset
voltages up to ±0.05 VDC

Input Hysteresis: 12 mV at 1 Hz

Low-Level AC Pulse Input Ranges:

Sine wave (mV RMS) Range (Hz)

20

200

2000

5000

1.0 to 20

0.5 to 200

0.3 to 10,000

0.3 to 20,000

Switch closure input

Terminals: C1-C8, P1-P2

Pull-Up Resistance: 100 kΩ to 5 V

Event: Low (<0.8 V) to High (>2.5 V)

Maximum Input Frequency: 150 Hz

Minimum Switch Closed Time: 5 ms

Minimum Switch Open Time: 6 ms

Maximum Bounce Time: 1 ms open without being counted

High-frequency input

Terminals: C1-C8, P1-P2

Pull-Up Resistance: 100 kΩ to 5 V

Event: Low (<0.8 V) to High (>2.5 V)

Maximum Input Frequency: 250 kHz

Digital input/output specifications

Terminals configurable for digital input and output (I/O)
including status high/low, pulse width modulation, external
interrupt, edge timing, switch closure pulse counting, high-
frequency pulse counting, plus UART1, RS-2322, RS-4223,

1Universal Asynchronous Receiver/Transmitter for asynchronous serial
communications.
2Recommended Standard 232. A loose standard defining how two computing
devices can communicate with each other. The implementation of RS-232 in
Campbell Scientific data loggers to computer communications is quite rigid,
but transparent to most users. Features in the data logger that implement RS-
232 communications with smart sensors are flexible.
3Communications protocol similar to RS-485. Most RS-422 sensors will work
with RS-485 protocol.

CR1000X Specifications | May 2, 2025

4

RS-4851, SDM2, SDI-123, I2C4, and SPI5 serial-communications
functions. Terminals are configurable in pairs for 5 V or 3.3 V
logic for some functions.

NOTE:
Conflicts can occur when a control port pair is used for
different instructions (TimerInput(), PulseCount(),
SDI12Recorder(), WaitDigTrig()). For example, if
C1 is used for SDI12Recorder(), C2 cannot be used for
TimerInput(), PulseCount(), or WaitDigTrig().

Terminals: C1-C8

Sustained Logic Input Voltage without Damage: ±20  VDC

Logic Levels and Drive Current:

Terminal pair configuration

5 V source

3.3 V source

Logic low

Logic high

C1 - C8

 ≤ 1.5 V

≥ 3.5 V

≤ 0.8 V

≥ 2.5 V

10 mA @ 3.5V 10 mA @ 1.85V

Edge timing

Terminals: C1-C8

Maximum Input Frequency: ≤ 1 kHz

Resolution: 500 ns

Edge counting

Terminals: C1-C8

Maximum Input Frequency: ≤ 2.3 kHz

Quadrature input

Terminals: C1-C8 can be configured as digital pairs to monitor
the two sensing channels of an encoder.

Maximum Frequency: 2.5 kHz

Minimum Pulse Width: 10 µs

Pulse-width modulation

Terminals: C1-C8

Maximum Period: 36.4 seconds

Resolution:

 l 0 – 5 ms: 83.33 ns
 l 5 – 325 ms: 5.33 µs
 l > 325 ms: 31.25 µs

1Recommended Standard 485. A standard defining how two computing
devices can communicate with each other.
2Synchronous Device for Measurement. A processor-based peripheral device
or sensor that communicates with the data logger via hardwire over a short
distance using a protocol proprietary to Campbell Scientific.
3Serial Data Interface at 1200 baud. Communications protocol for transferring
data between the data logger and SDI-12 compatible smart sensors.
4Inter-Integrated Circuit is a multi-controller, multi-peripheral, packet
switched, single-ended, serial computer bus.
5Serial Peripheral Interface - a clocked synchronous interface, used for short
distance communications, generally between embedded devices.

Communications specifications

Ethernet Port: RJ45 jack, 10/100Base Mbps, full and half duplex,
Auto-MDIX, magnetic isolation, and TVS surge protection.

Internet Protocols: Ethernet, PPP,  RNDIS, ICMP/Ping, Auto-IP
(APIPA), IPv4, IPv6, UDP, TCP, TLS (v1.2),  DNS, DHCP, SLAAC,
Telnet, HTTP(S), SFTP, FTP(S), POP3/TLS, NTP, SMTP/TLS,
SNMPv3, CS I/O IP, MQTT

Additional Protocols: CPI, PakBus, PakBus Encryption, SDM,
SDI-12, Modbus RTU / ASCII / TCP, DNP3 outstation, custom
user definable over serial, NTCIP, NMEA 0183, I2C, SPI

USB Device: Micro-B device for computer connectivity

CS I/O: 9-pin D-sub  connector to interface with Campbell
Scientific CS I/O peripherals.

SDI-12 (C1, C3, C5, C7): Four independent SDI-12 compliant
terminals are individually configured and meet SDI-12 Standard
v 1.4.

RS-485 (C5 to C8): One full duplex or two half duplex

RS-422 (C5 to C8): One full duplex or two half duplex

RS-232/CPI: Single RJ45 module port that can operate in one
of two modes: CPI or RS-232. CPI interfaces with Campbell
Scientific CDM measurement peripherals and sensors. RS-232
connects, with an adapter cable, to computer, sensor, or
communications devices serially.

CPI: One CPI bus. Up to 1 Mbps data rate. Synchronization of
devices to 5 μS. Total cable length up to 610 m (2000 ft). Up to
20 devices. CPI is a proprietary interface for communications
between Campbell Scientific data loggers and Campbell
Scientific CDM peripheral devices. It consists of a physical layer
definition and a data protocol.

Hardwired: Multi-drop, short haul, RS-232, fiber optic

Satellite: GOES, Argos, Inmarsat Hughes, Irridium

Standards compliance specifications

View compliance and conformity documents at
www.campbellsci.com/cr1000x

.

Test

Shock and vibration:

Applied
standard

MIL-STD 810G
methods 516.6
and 514.6

Description

Protection:

Wiring panel

Measurement module
when connected to
wiring panel

IP40

IP65

CR1000X Specifications | May 2, 2025

5

Test

Applied
standard

Description

EMI and ESD immunity:

ESD

 IEC 61000-4-2

Radiated RF

IEC 61000-4-3

EFT

Surge

IEC 61000-4-4

 IEC 61000-4-5

Conducted RF

IEC 61000-4-6

±15 kV air, ±8
kV contact
discharge

10 V/m, 80-
1000 MHz

4 kV power, 4
kV I/O

4 kV power,
4kV I/O

10 V power,
10 V I/O

Emissions and immunity performance criteria available on request.

Warranty

Standard: Three years against defects in materials and
workmanship.

Extended (optional): An additional four years, bringing the total
to seven years.

CR1000X Specifications | May 2, 2025

6

Terminal functions

Analog input terminal functions

SE
DIFF

 1   2
┌1┐
H   L

 3   4
┌2┐
H   L

 5   6
┌3┐
H   L

7   8
┌4┐
H   L

9  10
┌5┐
H   L

11  12
┌6┐
H   L

13  14
┌7┐
H   L

15  16
┌8┐
H   L

RG1

RG2

Single-Ended Voltage

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓

Differential Voltage

H

L

H

L

H

L

H

L

H

L

H

L

H

L

H

L

Ratiometric/Bridge

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓

Thermocouple

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓

Current Loop

✓

✓

Period Average

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓

Pulse counting terminal functions

Switch-Closure

High Frequency

Low-level AC

P1

✓

✓

✓

P2

C1-C8

✓

✓

✓

✓

✓

Analog output terminal functions

Switched Voltage Excitation

✓

VX1-VX4

Voltage Output

5 VDC

3.3 VDC

12 VDC

C1-C81

VX1-VX4

✓

✓

✓

✓

5V

✓

12V

SW12-1

SW12-2

✓

✓

✓

1C terminal voltage levels are configured in pairs. The default voltage output from C terminals is 5 V. Use the PortPairConfig instruction in
CRBasic to configure a C terminal pair to output 3.3 V.

Communications terminal functions

SDI-12

GPS

TTL 0-5 V1

LVTTL 0-3.3 V1

RS-232*

C1

✓

PPS

Tx

Tx

C2

Rx

Rx

Rx

C3

✓

Tx

Tx

Tx

C4

Rx

Rx

Rx

C5

✓

Tx

Tx

Tx

Tx

C6

Rx

Rx

Rx

Rx

C7

✓

Tx

Tx

Tx

Tx

C8

Rx

Rx

Rx

Rx

CR1000X Specifications | May 2, 2025

RS-
232/CPI

✓

7

Communications terminal functions

C1

C2

C3

C4

RS-485 (Half
Duplex)

RS-4852 (Full
Duplex)

I2C

SPI

SDM3

CPI/CDM

SCL

SCLK

Data

SDA

COPI

Clk

SCL

CIPO

Enabl

SDA

C5

A-

Tx-

SCL

SCLK

Data

C6

B+

Tx+

SDA

COPI

Clk

C7

A-

Rx-

SCL

CIPO

Enabl

C8

B+

Rx+

SDA

RS-
232/CPI

✓

*ComC1 and ComC3 on the CR1000X are not designed to handle RS-232 signals, and long-term exposure—such as when connecting an RV50(X)
modem—can damage the data logger.

1 TTL and LVTTL are configured with the CommsMode option of the SerialOpen instruction in CRBasic.

2 RS-422 compatible.

3 SDM can be on either C1-C3 or C5-C7, but not both at the same time.

Communications functions also include Ethernet and USB.

WARNING:
While ComC1–ComC3 are compatible with RS-232 signals on the CR1000Xe, only ComC5 and ComC7 are compatible with RS-
232 signals on the CR1000X. ComC1 and ComC3 on the CR1000X are not designed to handle RS-232 signals, and long-term
exposure—such as when connecting an RV50(X) modem—can damage the data logger. An advantage of the CR1000Xe is that
ComC1, ComC3, ComC5, and ComC7 all support RS-232 signals, whereas the CR1000X supports RS-232 only on ComC5 and
ComC7.

Digital I/O terminal functions

General I/O

Pulse-Width Modulation Output

Timer Input

Interrupt

Quadrature

C1-C8

✓

✓

✓

✓

✓

CR1000X Specifications | May 2, 2025

8

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


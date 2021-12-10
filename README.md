**MEMO Number SRS-Final-F21 DATE:** 29 November 2021

**TO:** EFC LaBerge

**FROM:** Faheel Kamran, Alina Momin, Ben Yamada, Tracy Yan

**SUBJECT:** System Requirements Specification Final

---

###  **1   INTRODUCTION**
#### **1.1 Purpose and Scope**

The purpose of this document is to provide requirements for a Self Organizing Drone Display (SODD) system. The scope of this document includes system overview requirements to be designed by the team, functional requirements that the SODD system must satisfy, and tests that will verify the system is functioning according to the requirements.

#### **1.2 Background**

Drone displays differ from fireworks in that drones are reusable and do not produce air or noise pollution. They offer a viable alternative in any situation where fireworks would be used.

#### **1.3 System Overview**

The SODD system has two types of subsystems, the Base Station Subsystem and the Individual Drone Subsystems. The Base Station Subsystem consists of a processing system, the software program, the controller, and the communication devices. Each drone is also a subsystem and consists of the drone itself, the mounting frame, and the lighting equipment. Each subsystem will be powered by their own battery. External to the SODD system is the user, who uses the controller to control the system, the battery chargers, to power the batteries for both the Base Station and the drones, the environment which impacts the flight of the drones, and the programming interface for the system, which will determine the functionality of the Base Station Subsystem and the Individual Drone Subsystems. Figure 1 shows the SODD system boundary diagram (SBD), which illustrates the SODD system, its subsystems, and the external inputs to the system.

![SBD](Aspose.Words.9320a93b-ab9c-4b9c-9259-27bdfe3610ec.002.jpeg)

*Figure 1: System Boundary Diagram*

The SODD system has four operational scenarios for the drone constellation. The first is a self-testing stage, during which the system tests if the communications between drones and between the drones and the controller are online. In the second scenario, the user enters a flight pattern for the drones to execute for a show, and in the third, the user enters a lighting pattern for the LEDs to follow. Finally, the fourth scenario has the system conduct a light show run on user input following the flight and lighting patterns entered into the system. Figure 2 shows the SODD mission scenario diagram (MSD).

![MSD](Aspose.Words.9320a93b-ab9c-4b9c-9259-27bdfe3610ec.003.jpeg)

*Figure 2: Mission Scenario Diagram*

Figure 3, below, shows the SODD  data flow diagram (DFD) and how the inputs and signals are used within the system. The user presses the ON/OFF button to turn on the system.

Once the user presses the TEST button, the central station (Hub) communication module begins a self-test and transmits a wake-up signal to the drones. At the end of the self-test, a system ready signal is transmitted to the Processing system.

The drone LEDs light up green after receiving the wake-up signal to signal their readiness. A Drone Ready signal is then transmitted to the Hub communication module responsible for transmitting the control signals.

The user enters an input into a software simulation to generate flight data and LED control data for a desired routine. This is sent to the central hub for processing and conversion into flight and LED commands. The system sends these commands to the Hub communication modules, which will transmit the drone control signals to the drones when the user presses the BEGIN button.

The drones will then execute the routine based on the control signals. The drones will send drone location signals to other drones to prevent drone collisions as well as to the Hub communication modules to track the drones.

![DFD](Aspose.Words.9320a93b-ab9c-4b9c-9259-27bdfe3610ec.004.jpeg)

*Figure 3: Data Flow Diagram*

#### **1.4 External Standards**

The SODD team will be held to the highest standards of ethical conduct by the Institute of Electrical and Electronics Engineers (IEEE) during the design, development, prototyping and demonstration of the project.

FAA Drone Guidelines, USC 44809 and Chapter 447 of Title 49 United States Code will be enforced during flight, navigation and operation of the drones.

Drone-to-Controller Communications will use Bluetooth V2.0+EDR, Bluetooth SPP: ETSI 07.10. RFCOMM.

Controller-Station Communications will use USB 2.0 Cable A/B specifications standard.

#### **1.5 Referenced Documents**

No referenced documents have been referred to at this time.

#### **1.6 Design Considerations**
#### **1.6.1 Global Considerations**

The SODD system will be designed based on North American standards for power, voltages and AC frequencies. For global use, adapters and different chargers will need to be considered for operation.

#### **1.6.2 Environmental Considerations**

There is less noise and light pollution from drones than fireworks. However, these pollutants may still be present. The reduced ecological footprint from the reusability of drones is the primary reason it is considered a viable alternative.

#### **1.6.3 Economic Considerations**

When compared to firework shows, creating drone shows will reduce the recurring fixed costs, since the drones can be reused. However, initial investment costs could  be higher as it includes purchasing drones and equipment, modifying, coding and implementing them to custom flight patterns, and developing the complete system.

#### **1.6.4 Cultural or Societal Considerations**

The drones can be used in festivals and celebrations. These can be holiday shows for 4th of July or New Years Eve, or ceremonies for wedding venues and other special occasions. The drones may also be used for educational purposes.

#### **1.6.5 Safety Considerations**

The team will have to follow FAA safety considerations on the altitude of the flight and consider how to prevent or mitigate possible injuries from falling drones, drone collisions, and LED lighting.

Baltimore-Washington International airport is an ICAO class B (busy) airport, this means that there will need to be specific precautions taken to fly the drones in the UMBC area. The team is aware that the drones will have to fly lower than 400 ft in the air and the drones will also have to follow a weight criteria.

#### **1.6.6 Cyber Security Considerations**

There is a concern of hacking to take control of the drones. For a final product, steps should be taken to mitigate the risk of hacking.

Should the team decide on a drone with a camera, they will disable and cover the camera to prevent possible hackers from using it.

###  **2   SYSTEM REQUIREMENTS**
#### **2.1 Functional Requirements**

The technical requirements necessary to implement the SODD are given in tabular form in figure 4. System 1-3 covers general system-related requirements. Power-On Self-Test (POST) 1-5 are requirements from turning the system on and running hardware diagnostic checks to ensure the systems are online and working. Test 1-2 cover requirements for this self-test. Lights 1-2 are lighting display requirements. Routine 1 includes the minimum requirement for the flight structure, while Flight 1-3 covers the route automation. Comms 1-2 depict the requirements for the communication systems. Chassis 1 is a requirement for any exterior structures required for the implementation of the project.

|ID|Title|Requirement|
| - | - | - |
|F01|SYSTEM 1|The system shall control a fleet of [four, five, six] simple drones.|
|F02|SYSTEM 2|The constellation shall automatically reconfigure itself to maintain a pre-stated distance from other drone members.|
|F03|SYSTEM 3|The constellation shall reconfigure the drone constellation to a specified shape through a triggered action, thereby overriding the configuration of F02.|
|F04|POST 1|The user shall power on/off the system(s) by pressing the ON/OFF button(s).|
|F05|POST 2|The system shall initiate self-test when the user presses the TEST button.|
|F05.1|POST 2.1|Each drone shall have a self-test mode that is triggered on startup and then executed once every [60] seconds.|
|F06|POST 3|Once powered on, the drone’s LED shall be red if the self-test is not initiated with the TEST button.|
|F07|POST 4|The drone’s LED shall remain red if it fails the self-test.|
|F08|TEST 1|The self-test shall generate a “wake-up” signal to be transmitted to the receiver(s).|
|F09|TEST 2|The self-test shall transmit “wake-up” signals to be received by the drone’s receivers if the receivers are functioning correctly.|
|F10|POST 5|The drone’s LED shall turn green when the receivers receive the 4-bit signal successfully and self-test has been completed.|
|F11|LIGHTS 1|The system shall be able to wirelessly control drone LEDs via a command sequence protocol using bluetooth transceivers.|
|F12|LIGHTS 2|The command sequence shall be able to independently control at least 256 states for each of three colors ( R, G, and B).|
|F13|ROUTINE 1|The controller shall permit creation and editing of flight routines. At a minimum, the controller shall permit control of the desired geometry and the LED colors.|
|F14|FLIGHT 1|The user shall initiate the flight routine to start by pressing the BEGIN button.|
|F15|FLIGHT 2|The drone’s initial configuration shall be in a horizontal line.|
|F16|FLIGHT 3|The drones shall follow a flight routine configured to a specified geometry shape to form a constellation.|
|F17|COMMS 1|The drones shall communicate with the drone-controller station using transceivers.|
|F18|COMMS 2|The communication systems shall use existing wireless IEEE standards.|
|F19|CHASSIS 1|The drone shall have a chassis frame to attach the lighting display.|

*Figure 4: Functional Requirements Table*

#### **2.2 Performance Requirements**

The performance requirements necessary to implement the SODD are given in tabular form in figure 5.

|ID|Title|Requirement|
| - | - | - |
|P01|LIGHTS 1|The lights shall be at least [160] lumens to be visible at the drone’s highest possible altitude of [50 meters].|
|P02|COMMS 1|The system shall be able to cover inter-drone distances of at least 50 meters.|
|P03|FLIGHT 1|The system shall be able to follow its pre-planned route with a circular positioning error of [1 meter] 95% of the time. Circular positioning error shall not exceed [2 meters] in any case.|
|P04|TEST 1|The drones LED’s shall be able to represent the proper color configuration that corresponds to the self-test.|
|P05|SYSTEM 1|The prototype drone display shall run for at least [two] minutes.|
|P06|SYSTEM 2|The drones shall remain at minimum [one, two] meter(s) apart for safety considerations.|
|P07|CHASSIS 1|The LED fixture on each drone shall not exceed [50%] of the drone’s maximum lifting capacity .|

*Figure 5: Performance Requirements Table*

#### **2.3 Interface Requirements**

The interface requirements necessary to implement the SODD are given in tabular form in figure 6.

C-2-D COM: Controller to Drone Communications D-2-D COM: Drone to Drone Communications

|ID|Title|Requirement|
| - | - | - |
|I01|C-2-D COM 1|The main station shall transmit control signals to the drones, through a bluetooth enabled microcontroller, using the drone’s software development kit (SDK).|
|I02|C-2-D COM 2|The drones shall transmit their location data to the main station, through the drone’s bluetooth capabilities, using predefined tracking modules from in the drone’s SDK.|
|I03|D-2-D COM 1|The drones shall also transmit their locations to each other during flight using the tracking enabled SDK to maintain a safe distance apart as specified in P06.|

*Figure 6: Interface Requirements Table*

#### **2.4 Testing Requirements**

The testing requirements necessary to implement the SODD are given in tabular form in figure 7.


|ID|Title|Requirement|
| - | - | - |
|T01|TEST 01|The fleet shall be tested indoors in a dark environment.|
|T02|TEST 02|The drone fleet will be tested for consistent flight.|

*Figure 7: Testing Requirements Table*

#### **2.5 Design Requirements**

The design requirements necessary to implement the SODD are given in tabular form in figure 8.

|ID|Title|Requirement|
| - | - | - |
|D01|SAFETY 1|The system shall obey all FAA Unmanned Aircraft Systems regulations.|
|D02|COST 1|The system shall not exceed a budget of $400.|

*Figure 8: Design Requirements Table*

### **3  VERIFICATION**

The steps to verify the above requirements are given in tabular form in figure 9. For a requirement to be tested, it must be a quantifiable measurement of a characteristic of the system. For a requirement to be demonstrated, it must be a qualitative observation that the system performs a function or has a given characteristic. For a requirement to be inspected, it must be a quality observed in the system. For a requirement to be analyzed, it must be determined mathematically.

|ID|Requirement|Test|Demo|Inspection|Analysis|
| - | - | - | - | - | - |
|V01|F01|X|X|||
|V02|F02||X|X||
|V03|F03||X|X||
|V04|F04||X|||
|V05|F05||X|||
|V06|F06|||X||
|V07|F07||X|X||
|V08|F08||||X|
|V09|F09|X|X||X|
|V10|F10|||X||
|V11|F11||X|||
|V12|F12||X||X|
|V13|F13||X|||
|V14|F14||X|||
|V15|F15||X|X||
|V16|F16||X|X||
|V17|F17||X||X|
|V18|F18||||X|
|V19|F19|||X||
|ID|Requirement|Test|Demo|Inspection|Analysis|
|V20|P01|||X||
|V21|P02|X||||
|V22|P03||X|X||
|V23|P04||X|X||
|V24|P05|X||||
|V25|P06|X||||
|V26|P07|||X||
|ID|Requirement|Test|Demo|Inspection|Analysis|
|V27|I01||X|||
|V28|I02|X||||
|V29|I03|X||||

*Figure 9: Verification Table*

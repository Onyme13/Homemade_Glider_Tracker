# Homemade Glider Computer (Work in progress)

In the world of light aviation and air sports, gliders occupy a special place because of their dependence on the weather and their ability to slide silently across the skies. To improve the flying experience of gliders and provide pilots with essential data in real time, My bachelor’s degree research project in Information Systems and Service Science focused on the design and implementation of a prototype homemade flight tracker specifically designed for these aircraft.


**WARNING: PROTOTYPE**

This device is an experimental prototype and should only be used for testing purposes. It is not intended for flight-critical applications or navigation. Use at your own risk. The creator is not responsible for any accidents or damages resulting from its use. Prioritize safety and follow all aviation regulations during testing.

## Installation


**Step 1: Gather the Required Materials**

Before starting the installation process, make sure you have all the necessary materials and components for your homemade glider computer. These may include:

1. Raspberry Pi Zero W (the WiFi model in important for ssh connection for future installations)
2. MicroSD card (at least 32GB)
3. Arduino Micro without headers
4. GPS Module
5. Antenna for the GPS module (not mandatory)
6. Barometric sensor
7. Display (TFT screen 3.5")
8. PiSugar Battery for Raspberry Pi-Zero W/WH 1200 mAh
9. Cables and connectors
10. micro-USB to micro-USB cable
11. Case to mount the components securely (Can be 3D printed).
    You can find the .stl file for the case and the cover on this repository.
(12. Two 2mm screws for closing the case, if 3D printed)

See the [Required Materials](https://github.com/Onyme13/Homemade_Glider_Tracker/tree/main/Documentation) for more informations about all the necessary materials.

**Step 2: Set Up the Raspberry Pi**

For more information. Follow the [Manuel_de_reproduction_FR.pdf](https://github.com/Onyme13/Homemade_Glider_Tracker/blob/main/Documentation/Manuel_de_reproduction_FR.pdf) for more details. Pages 6 to 11

1. Download the latest Raspberry Pi OS Imager from the official website.
2. Flash the OS image onto a microSD. In the Advanced option, enable SSH for remote connection. It is the only way to access to the Pi.
3. Download Advanced IP Scanner from the official website.
4. Download PuTTY - a free SSH and telnet client for Windows. (Or any other SSH solution)
5. Download FileZilla - The free File Transfert Protocol solution. You need this to upload your GPS map to the Pi.
5. Setup the Raspeberry Pi OS . Follow the [Manuel_de_reproduction_FR.pdf] guide. Pages 7 to 10
6. Insert the microSD card into the Raspberry Pi.


**Step 3: Install Required Software on the Raspberry PI using SSH**

For more information. Follow the [Manuel_de_reproduction_FR.pdf](https://github.com/Onyme13/Homemade_Glider_Tracker/blob/main/Documentation/Manuel_de_reproduction_FR.pdf) for more details. Pages 12 to 17

(This is probably the longest step of the installation)


1. Power up the Raspberry Pi.

2. Scan all the IP's from your network with Advanced IP Scanner so you can the Raspberry Pi's IP address.

3. With the now found IP adress. Connect to your Raspberry Pi through SSH with PuTTY. 

4. Update the Raspberry Pi OS by running:
   ```
   sudo apt-get update
   sudo apt-get upgrade
   ```

5. Clone the git repository by running.
    ```
    git clone https://github.com/Onyme13/Homemade_Glider_Tracker.git
    ```
6. Install Pip and go in to the file. After installation of pip, you can verify that pip is installed:
    ```
    sudo apt install python3-pip
    pip --version
    ```

   Then install the needed python libraries:

    ```
    cd Research-Project
    sudo python -m pip install -r requirements.txt
    ```    

7. File transfert the map zipped file using FileZilla (this step can take more than hour).

8. Unzip the file by running on the Raspberry Pi (this step can take more than hour):
    ```
    sudo apt install unzip
    unzip tile_OSM.zip
    ```
9. Meanwhile configure the screen by activating SPI connection on the Pi and disable Sleep Mode , run:
    ``` 
    sudo raspi-config
    ```
10. Navigate to Display Options, and press enter.
11. Navigate to the 4th line, Screen Blanking. Press Enter and select No.
12. Activate the SPI connection on the same menu.
13. Then run:
    ```
    sudo rm -rf LCD-show
    git clone https://github.com/MrYacha/LCD-show.git
    chmod -R 755 LCD-show
    cd LCD-show/
    ```
    and 
    ```
    sudo ./LCD35-show
    ```
    The Pi will reboot, the screen should be correctly configured



**Step 4: Set Up the Microcontroller Arduino Micro**

1. Download the Arduino IDE from the official website
2. Connect your microcontroller to your computer with USB
3. Upload the Arduino_Double_Sensor.ino from this repository on the Arduino Micro with the Arduino IDE using your computer.

**Step 5: Assemble the Components**
Carefully solder all the connectors following the schema. Adapt the cabling according to your components.

Follow the [Manuel_de_reproduction_FR.pdf](https://github.com/Onyme13/Homemade_Glider_Tracker/blob/main/Documentation/Manuel_de_reproduction_FR.pdf) steps.

Double-check the schema (wiring diagram) to ensure you have a clear understanding of how the connectors should be soldered. The schema will show the connections between different components, such as sensors, displays, and microcontrollers.

Carefully mount the Raspberry Pi, microcontroller, sensors, display, and other components inside the case. 

**Step 6: Test the Glider Computer Software**

Verify that the software is working as expected. Make sure the data from sensors are accurate, the display shows the relevant information correctly, and the system behaves as intended.

**Step 7: Test the Glider Computer**

ALWAYS PRIORITIZE THE FLIGHT SAFETY.
KEEP YOUR EYES OUT OF THE PLANE.

Before the actual glider flight, do some ground tests to confirm that the glider computer works as expected. Once you're confident in its functionality, conduct a test flight to see how it performs during actual gliding.

**Step 8: Monitor and Improve**

ALWAYS PRIORITIZE THE FLIGHT SAFETY.
KEEP YOUR EYES OUT OF THE PLANE.

During and after the flight, closely monitor the glider computer's performance. Take note of any issues or improvements that can be made to enhance its functionality or accuracy.

Remember to always prioritize safety and adhere to local regulations.


## Contributing

Thank you for considering contributing to Homemade Glider Computer! I welcome contributions from the community and appreciate your support in making this project better.


1. Clone the repository

2. Make Changes

Make your desired changes and improvements to the codebase. Please ensure that your changes adhere to the project's coding standards and guidelines.

3. Test your Changes

Before submitting a pull request, make sure to test your changes thoroughly to ensure they work as intended and do not introduce any new issues.ct.

4. Commit your changes

5. Code Review

Your pull request will undergo a code review by the project maintainers. Be prepared to make additional changes based on feedback.

6. Merge

Once your pull request is approved and any necessary changes are made, it will be merged into the main project.


Thank you for your valuable contributions!


## License

This work is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## Contact

For any questions, feel free to contact me at this email adress: jocorl@hotmailch

## Photos

<img src="/images/readme/log1.jpg" width="200">

<img src="/images/readme/art1.jpg" width="200">

<img src="/images/readme/art2.jpg" width="200">

<img src="/images/readme/test1.jpg" width="200">

<img src="/images/readme/test2.jpg" width="200">

## Further Reading

FacLab articles
1. [Développement d'un Tracker de Vol Fait Maison pour Planeurs](https://faclab.ch/publication/developpement-dun-tracker-de-vol-fait-maison-pour-planeurs)
2. [Tests et conclusion du travail de Bachelor du Tracker de Vol Fait Maison pour Planeurs](https://faclab.ch/publication/tests-et-conclusion-du-travail-de-bachelor-du-tracker-de-vol-fait-maison-pour-planeurs)

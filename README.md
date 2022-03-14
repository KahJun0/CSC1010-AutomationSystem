# CSC1010-AutomationSystem
Python files for CSC1010 project.

### Requirements

>paho.mqtt

>pigpio

You will also need to enable camera controls using
> sudo rasp-config

Select Interface Options, Camera Port and select Enabled. You can now exit. This may cause your Pi to reboot.

You can make sure that the camera module is all working well by taking a picture via the Pi camera module by running this in the below terminal command:
> raspistill -o Desktop/image.jpg

### Breakdown of files in the repo
- Profile Folder – Where all Face recognition profiles are stored.
- Templates Folder – This is where the HTML webpage would be stored
- Python script:
- Camera.py – The script access open CV and the face recognition library to identify persons from its encoding matrix.
- main.py – Where the Flask stream is created – camera.py

Demo Python Scripts:
- facerec_pi_test.py – Test script to detect faces
- face_pi_test_profiles.py – Test script to detect multiple faces.


### Running it
To run, do
>python main.py GPIO_PIN_CONNECTED_TO_SERVO

### Other notes

MFRC522.py has been modified to work with pigpio but the values of the SPI GPIO has been hardcoded to 22.
You will need to change this if yours differ.

Keep in mind that to install the camera stream dependencies you will require to install face-recognition package, which could take about 40mins to install. Refer to it here: https://smartbuilds.io/installing-face-recognition-library-on-raspberry-pi-4/ 

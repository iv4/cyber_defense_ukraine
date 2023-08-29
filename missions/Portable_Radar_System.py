
import time

def run(player):
    print(f"{player.green}Mission: Creating a Portable Radar System{player.reset}")
    print(f"{player.yellow}Background: Your team needs to set up a portable radar system to monitor enemy movement. Your mission is to create this system using Arduino or Raspberry Pi with ultrasonic sensors.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in a remote location and you have the hardware with you. Your first task is to assemble the hardware.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Choose the hardware to assemble.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Arduino, Raspberry Pi, None] What hardware will you use: {player.reset}")
    
    if task1_choice.lower() == "arduino":
        print(f"{player.green}Great choice! Arduino is suitable for this mission. You will need an HC-SR04 ultrasonic sensor for this setup. Connect the sensor's VCC to 5V on the Arduino, GND to GND, Trig to Digital pin 9, and Echo to Digital pin 10.{player.reset}")
        player.inventory.append("Arduino Setup")
    elif task1_choice.lower() == "raspberry pi":
        print(f"{player.green}Great choice! Raspberry Pi is also suitable for this mission. You will need a GPIO Ultrasonic Sensor. Connect VCC to 5V, GND to GND, Trig to GPIO 17, and Echo to GPIO 18.{player.reset}")
        player.inventory.append("Raspberry Pi Setup")
    else:
        print(f"{player.red}Poor choice! Without appropriate hardware, you can't proceed with the mission.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: Your hardware is ready. Now it's time to upload the code to the board.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Choose the software to upload code.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [Arduino IDE, Python Script, None] What software will you use: {player.reset}")
    
    if task2_choice.lower() == "arduino ide":
        print(f"{player.green}Excellent! Arduino IDE is perfect for uploading code to Arduino. You write a simple sketch that uses the 'NewPing' library to read data from the HC-SR04 sensor. To install the library, go to Sketch -> Include Library -> Manage Libraries and search for 'NewPing'.{player.reset}")
        player.inventory.append("Arduino IDE Setup")
    elif task2_choice.lower() == "python script":
        print(f"{player.green}Excellent! Python is perfect for Raspberry Pi. You will use the 'RPi.GPIO' library to control the GPIO pins. Install it using 'pip install RPi.GPIO'. Your script will read data from the ultrasonic sensor and print it to the console.{player.reset}")
        player.inventory.append("Python Script Setup")
    else:
        print(f"{player.red}Poor choice! Without appropriate software, you can't proceed with the mission.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: Your radar system is operational. Now it's time to test it.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Test the radar system.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [Start Test, Calibrate, None] What will you do: {player.reset}")
    
    if task3_choice.lower() == "start test":
        print(f"{player.green}Success! Your radar system detects an object moving at a distance of 500 meters. Mission accomplished!{player.reset}")
        player.inventory.append("Mission Accomplished Badge")
    elif task3_choice.lower() == "calibrate":
        print(f"{player.green}Good idea! Calibration ensures the system's accuracy. You fine-tune the sensor's sensitivity and retest. It's now even more accurate.{player.reset}")
        player.inventory.append("Calibration Badge")
    else:
        print(f"{player.red}Mission failed! Without a successful test, the mission is incomplete.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Creating a Portable Radar System' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

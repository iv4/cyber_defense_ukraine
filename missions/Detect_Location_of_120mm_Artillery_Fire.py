
import time

def run(player):
    print(f"{player.green}Mission: Creating a System to Detect the Location of 120mm Artillery Fire{player.reset}")
    print(f"{player.yellow}Background: Your team is under artillery fire and needs to identify the source quickly to neutralize it. Your mission is to set up a sound triangulation system using available hardware and software.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in a forward observation post with limited equipment. You need to improvise a system for artillery detection.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Choose the hardware to use for this mission.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Microphone Array, Single Microphone, Pressure Sensors, None] What hardware will you use: {player.reset}")
    
    if task1_choice.lower() == "microphone array":
        print(f"{player.green}Excellent choice! A microphone array can pick up sound from multiple directions, making it ideal for triangulating artillery fire. Connect the microphone array to a Raspberry Pi via USB. Then, you'd need to install 'Audacity' for sound analysis. Run 'sudo apt-get install audacity' to install it.{player.reset}")
        player.inventory.append("Microphone Array")
    else:
        print(f"{player.red}Poor choice! The selected hardware is not suitable for this mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: The hardware is set up. Now, you need to calibrate the system to pick up the sound of 120mm artillery fire specifically.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Calibrate the microphone array.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [High Gain, Low Gain, Auto Gain, None] How will you set the microphone gain: {player.reset}")
    
    if task2_choice.lower() == "high gain":
        print(f"{player.green}Great choice! High gain settings will make the microphone more sensitive, allowing it to pick up distant sounds like artillery fire. Use 'Audacity' to record a sample and analyze the frequency. Artillery fire usually falls within the 20-200 Hz range. Filter out other noises using a band-pass filter in Audacity.{player.reset}")
        player.inventory.append("High Gain Settings")
    else:
        print(f"{player.red}Poor choice! Your system is not calibrated correctly. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: The system is calibrated and ready to triangulate the location of the artillery.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Triangulate the source of the artillery fire.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [Start, Test, Abort, None] What will you do: {player.reset}")
    
    if task3_choice.lower() == "start":
        print(f"{player.green}Mission accomplished! You've successfully triangulated the source of the artillery fire. The Python script you wrote uses the 'numpy' library to perform Fast Fourier Transform (FFT) to analyze the sound spectrum. Run 'pip install numpy' to install it. Your script also uses 'sounddevice' for real-time audio input. Install it using 'pip install sounddevice'.{player.reset}")
        player.inventory.append("Mission Accomplished Badge")
    else:
        print(f"{player.red}Mission failed! You were unable to triangulate the source. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Creating a System to Detect the Location of 120mm Artillery Fire' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

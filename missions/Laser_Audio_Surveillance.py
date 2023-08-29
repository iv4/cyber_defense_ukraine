
import time

def run(player):
    print(f"{player.green}Mission: Laser-Based Audio Surveillance{player.reset}")
    print(f"{player.yellow}Background: Enemy generals are planning a troop movement, and you need to gather intelligence. Your mission is to set up a laser-based audio surveillance system to listen in on their conversation through a glass window.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're stationed near the enemy base with your equipment. First, you need to set up the laser and photo-detector.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Assemble the laser and photo-detector setup.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Assemble, Skip, Abort] What will you do: {player.reset}")
    
    if task1_choice.lower() == "assemble":
        print(f"{player.green}You successfully assemble the laser diode, align it towards the glass window, and set up the photo-detector at an angle where it can receive the reflected laser light. You connect it to an amplifier circuit to boost the signal.{player.reset}")
        player.inventory.append("Laser and Photo-Detector Setup")
    else:
        print(f"{player.red}Mission failed! Without assembling the equipment, you cannot proceed.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: Your hardware is ready. You now need to set up the software to record the audio.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Choose the software to record the audio.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [Audacity, Python Script, Abort] What software will you use: {player.reset}")
    
    if task2_choice.lower() == "audacity":
        print(f"{player.green}Excellent choice! Audacity is great for audio recording. You set it up to record from the input connected to the amplifier circuit and start monitoring.{player.reset}")
        player.inventory.append("Audacity Setup")
    elif task2_choice.lower() == "python script":
        print(f"{player.green}Excellent choice! You write a Python script using the 'sounddevice' library to capture audio input. You install the library using 'pip install sounddevice'.{player.reset}")
        player.inventory.append("Python Script Setup")
    else:
        print(f"{player.red}Mission failed! Without setting up the software, you cannot proceed.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: Your surveillance system is operational. Now it's time to gather intelligence.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Gather intelligence.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [Start Recording, Calibrate, Abort] What will you do: {player.reset}")
    
    if task3_choice.lower() == "start recording":
        print(f"{player.green}Success! You start recording and soon hear the enemy generals discussing troop movements. You have successfully gathered crucial intelligence.{player.reset}")
        player.inventory.append("Mission Accomplished Badge")
    elif task3_choice.lower() == "calibrate":
        print(f"{player.green}Good idea! Calibration ensures the system's accuracy. You adjust the laser alignment and fine-tune the amplifier settings, then start recording. The audio is now crystal clear.{player.reset}")
        player.inventory.append("Calibration Badge")
    else:
        print(f"{player.red}Mission failed! Without gathering intelligence, the mission is incomplete.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Laser-Based Audio Surveillance' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

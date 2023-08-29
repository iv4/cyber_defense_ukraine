
import time

def run(player):
    print(f"{player.green}Mission: Flooding Enemy Radio Comms{player.reset}")
    print(f"{player.yellow}Background: To disrupt enemy coordination, you are tasked with setting up a battery-powered system that will flood their radio communications with the Ukrainian National Anthem 'Glory to Ukraine' at a pre-set time.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You are in a secure location with the necessary equipment. Your first task is to set up the hardware.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Assemble the Raspberry Pi, FM transmitter, and battery.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Assemble, Skip, Abort] What will you do: {player.reset}")
    
    if task1_choice.lower() == "assemble":
        print(f"{player.green}You successfully connect the Raspberry Pi to the FM transmitter and attach it to a battery. The hardware setup is now complete.{player.reset}")
        player.inventory.append("Hardware Setup")
    else:
        print(f"{player.red}Mission failed! Without assembling the hardware, you cannot proceed.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: With the hardware ready, it's time to upload the Ukrainian National Anthem and write a Python script to play it.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Upload the anthem and write the script.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [Upload and Write, Skip, Abort] What will you do: {player.reset}")
    
    if task2_choice.lower() == "upload and write":
        print(f"{player.green}You upload the Ukrainian National Anthem to the Raspberry Pi and write a Python script using the 'pygame' library to play it. You install the library using 'pip install pygame'.{player.reset}")
        player.inventory.append("Anthem and Script")
    else:
        print(f"{player.red}Mission failed! Without uploading the anthem and writing the script, you cannot proceed.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: The system is almost ready. Your final task is to schedule the anthem to play at a pre-set time.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Schedule the anthem to play.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [Schedule, Calibrate, Abort] What will you do: {player.reset}")
    
    if task3_choice.lower() == "schedule":
        print(f"{player.green}You successfully schedule the anthem to play at the desired time using a cron job. The mission is complete!{player.reset}")
        player.inventory.append("Scheduled Anthem")
    elif task3_choice.lower() == "calibrate":
        print(f"{player.green}Good idea! Calibration ensures the system's accuracy. You adjust the FM transmitter settings to match the enemy's radio frequency and then schedule the anthem. The mission is complete!{player.reset}")
        player.inventory.append("Calibration and Schedule")
    else:
        print(f"{player.red}Mission failed! Without scheduling the anthem, the mission is incomplete.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Flooding Enemy Radio Comms' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

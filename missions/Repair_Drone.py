
import time

def run(player):
    print(f"{player.green}Mission: Repairing a Shot-Down Drone{player.reset}")
    print(f"{player.yellow}Background: A surveillance drone has been shot down over hostile territory. Your mission is to repair it and retrieve the valuable data it holds.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You've reached the crash site and find the drone in a damaged state.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Assess the damage to the drone's hardware.{player.reset}")
    task1_choice = input(f"{player.blue}Commands: [assess --hardware, assess --skip, abort] What will you do: {player.reset}")
    
    if task1_choice.lower() == "assess --hardware":
        print(f"{player.green}You assess the hardware and identify a damaged propeller and a malfunctioning camera.{player.reset}")
        player.inventory.append("Damaged Hardware Assessment")
    else:
        print(f"{player.red}Mission failed! You can't proceed without assessing the damage.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: After assessing the hardware, you need to repair the drone.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Repair the drone's damaged propeller and camera.{player.reset}")
    task2_choice = input(f"{player.blue}Commands: [repair --propeller, repair --camera, abort] What will you do: {player.reset}")
    
    if task2_choice.lower() == "repair --propeller" or task2_choice.lower() == "repair --camera":
        print(f"{player.green}You successfully repair the damaged parts. The drone is now operational!{player.reset}")
        player.inventory.append("Repaired Drone")
    else:
        print(f"{player.red}Mission failed! You can't proceed without repairing the drone.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: With the drone repaired, it's time to retrieve the stored data.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Retrieve the data from the drone's internal storage.{player.reset}")
    task3_choice = input(f"{player.blue}Commands: [retrieve --data, retrieve --skip, abort] What will you do: {player.reset}")
    
    if task3_choice.lower() == "retrieve --data":
        print(f"{player.green}You successfully retrieve the data from the drone's internal storage. Mission accomplished!{player.reset}")
        player.inventory.append("Retrieved Data")
    else:
        print(f"{player.red}Mission failed! Without retrieving the data, the mission is incomplete.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Repairing a Shot-Down Drone' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

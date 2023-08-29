
import time

def run(player):
    print(f"{player.green}Mission: UAV Defense{player.reset}")
    print(f"{player.yellow}Background: Enemy forces are deploying UAVs for aerial surveillance. Your mission is to disrupt and ground these UAVs.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You are at the defense command center with access to anti-UAV systems.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: What method will you use to detect incoming UAVs?{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Radar, Acoustic Sensors, Visual Cameras, Thermal Imaging] Choose your method: {player.reset}")
    
    if task1_choice.lower() == "radar":
        print(f"{player.green}Great choice! You successfully detect incoming UAVs.{player.reset}")
        player.inventory.append("UAV Detection")
    else:
        print(f"{player.red}You failed to detect the UAVs. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: You've detected the UAVs and now need to jam their signals.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: What frequency band will you jam to disrupt the UAVs?{player.reset}")
    task2_choice = input(f"{player.blue}Options: [2.4 GHz, 5 GHz, 900 MHz, 1.2 GHz] Choose your frequency: {player.reset}")
    
    if task2_choice.lower() == "2.4 ghz":
        print(f"{player.green}Successful jamming! The UAVs are starting to lose control.{player.reset}")
        player.inventory.append("Signal Jamming")
    else:
        print(f"{player.red}Jamming failed! The UAVs are still operational. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: One UAV is still operational and approaching fast. Time to ground it.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: What Python script will you use to hijack the UAV?{player.reset}")
    task3_choice = input(f"{player.blue}Options: [uav_hijack.py, skyjack.py, dronejack.py, none] Choose your script: {player.reset}")
    
    if task3_choice.lower() == "skyjack.py":
        print(f"{player.green}UAV hijacked! You successfully ground the UAV.{player.reset}")
    else:
        print(f"{player.red}Hijacking failed! The UAV is still operational. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'UAV Defense' completed successfully!{player.reset}")
    player.inventory.append("UAV Defense Badge")


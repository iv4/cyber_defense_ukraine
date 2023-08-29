
import time

def run(player):
    print(f"{player.green}Mission: Signal Triangulation{player.reset}")
    print(f"{player.yellow}Background: Enemy forces are using hidden radio transmitters to coordinate attacks. Your mission is to locate and neutralize these transmitters.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You are at the mobile signal tracking center with access to triangulation equipment.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: What type of antenna will you use for signal triangulation?{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Omni-Directional, Yagi, Parabolic, None] Choose your antenna: {player.reset}")
    
    if task1_choice.lower() == "yagi":
        print(f"{player.green}Excellent choice! Yagi antennas are great for directional signal tracking.{player.reset}")
        player.inventory.append("Yagi Antenna")
    else:
        print(f"{player.red}Poor choice! You failed to pick up any signals. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: You've picked up a suspicious signal and need to find its source.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: What triangulation method will you use?{player.reset}")
    task2_choice = input(f"{player.blue}Options: [Lateration, Angulation, RSSI, None] Choose your method: {player.reset}")
    
    if task2_choice.lower() == "lateration":
        print(f"{player.green}Correct! You're able to pinpoint the location of the transmitter.{player.reset}")
        player.inventory.append("Triangulation Method")
    else:
        print(f"{player.red}Incorrect method! You're unable to locate the transmitter. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: You've located the transmitter. Time to neutralize it.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: What command will you use to disrupt the signal?{player.reset}")
    task3_choice = input(f"{player.blue}Enter the command: {player.reset}")
    
    if task3_choice.lower() == "sudo jammer -f 2.4ghz":
        print(f"{player.green}Transmitter neutralized! Mission successful.{player.reset}")
    else:
        print(f"{player.red}Command failed! The transmitter is still active. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Signal Triangulation' completed successfully!{player.reset}")
    player.inventory.append("Signal Triangulation Badge")


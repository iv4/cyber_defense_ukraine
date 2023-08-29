
import time

def run(player):
    print(f"{player.green}Mission: Locate Civilians Using Cell Phone and WiFi Signals{player.reset}")
    print(f"{player.yellow}Background: Civilians are trapped in a conflict zone. Your mission is to locate them using cell phone and WiFi signals to coordinate a rescue.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in the operations center with access to software like Wireshark and a Software Defined Radio (SDR).{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Capture WiFi packets using Wireshark to identify any active civilian devices.{player.reset}")
    task1_choice = input(f"{player.blue}Commands: [wireshark --capture, wireshark --skip, abort] What will you do: {player.reset}")
    
    if task1_choice.lower() == "wireshark --capture":
        print(f"{player.green}You successfully capture WiFi packets and identify a number of active civilian devices.{player.reset}")
        player.inventory.append("WiFi Packets")
    else:
        print(f"{player.red}Mission failed! You can't proceed without capturing the WiFi packets.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: With the WiFi packet data, you now need to triangulate their location using the SDR.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Use the SDR to triangulate the location of the civilian devices.{player.reset}")
    task2_choice = input(f"{player.blue}Commands: [sdr --triangulate, sdr --skip, abort] What will you do: {player.reset}")
    
    if task2_choice.lower() == "sdr --triangulate":
        print(f"{player.green}Using the SDR, you triangulate the locations of the civilian devices. Coordinates acquired!{player.reset}")
        player.inventory.append("Coordinates")
    else:
        print(f"{player.red}Mission failed! You can't proceed without triangulating the locations.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: Coordinates in hand, it's time to send in the rescue team.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Transmit the coordinates to the rescue team using a secure channel.{player.reset}")
    task3_choice = input(f"{player.blue}Commands: [transmit --secure, transmit --open, abort] What will you do: {player.reset}")
    
    if task3_choice.lower() == "transmit --secure":
        print(f"{player.green}You successfully transmit the coordinates using a secure channel. The rescue team is on the way!{player.reset}")
        player.inventory.append("Successful Transmission")
    else:
        print(f"{player.red}Mission failed! Without transmitting the coordinates, the mission is incomplete.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Locate Civilians Using Cell Phone and WiFi Signals' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

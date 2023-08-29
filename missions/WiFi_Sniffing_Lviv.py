
import time

def run(player):
    print(f"{player.green}Mission: WiFi Sniffing (Lviv){player.reset}")
    print(f"{player.yellow}Background: Your mission is to sniff WiFi packets to detect rogue devices in Lviv.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You are at the cyber defense unit in Lviv with access to WiFi sniffing equipment.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: What Python library will you use for WiFi sniffing?{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Scapy, Wireshark, PyShark, None] Choose your library: {player.reset}")
    
    if task1_choice.lower() == "scapy":
        print(f"{player.green}Excellent choice! Scapy is a powerful Python library for packet manipulation.{player.reset}")
        player.inventory.append("Scapy Library")
    else:
        print(f"{player.red}Incorrect choice! You're unable to sniff any WiFi packets. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: You've started sniffing WiFi packets and suspect there might be rogue devices.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: What filter will you apply to narrow down the packets?{player.reset}")
    task2_choice = input(f"{player.blue}Options: [SSID, MAC Address, Channel, None] Choose your filter: {player.reset}")
    
    if task2_choice.lower() == "mac address":
        print(f"{player.green}Smart move! Filtering by MAC address will help you detect rogue devices quickly.{player.reset}")
        player.inventory.append("MAC Address Filter")
    else:
        print(f"{player.red}Incorrect filter! You're unable to detect any rogue devices. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: You've narrowed down the packets and suspect a few MAC addresses to be rogue devices.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Enter the suspected rogue MAC addresses.{player.reset}")
    task3_choice = input(f"{player.blue}Enter the MAC addresses separated by commas: {player.reset}")
    
    if "00:11:22:33:44:55" in task3_choice.replace(" ", "").split(","):
        print(f"{player.green}You've successfully identified a rogue device! Mission successful.{player.reset}")
    else:
        print(f"{player.red}You failed to identify the rogue devices. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'WiFi Sniffing (Lviv)' completed successfully!{player.reset}")
    player.inventory.append("WiFi Sniffing Badge")


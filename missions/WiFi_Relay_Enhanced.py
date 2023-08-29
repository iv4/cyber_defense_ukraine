
import time

def run(player):
    print(f"{player.green}Mission: Creating a Portable WiFi Signal Relay{player.reset}")
    print(f"{player.yellow}Background: Your team is in a dense urban area with limited communication. Your mission is to create a portable WiFi signal relay using a Raspberry Pi and OpenWRT to extend the lines of communication.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in a makeshift lab with a Raspberry Pi, an SD card, and a USB WiFi dongle.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Flash OpenWRT onto the SD card to turn the Raspberry Pi into a WiFi extender.{player.reset}")
    task1_choice = input(f"{player.blue}Commands: [dd if=openwrt.img of=/dev/sdX, abort] What will you do: {player.reset}")
    
    if task1_choice.lower() == "dd if=openwrt.img of=/dev/sdx":
        print(f"{player.green}You successfully flashed OpenWRT onto the SD card. Insert it into the Raspberry Pi.{player.reset}")
        player.inventory.append("Flashed SD Card")
    else:
        print(f"{player.red}Mission failed! You can't proceed without flashing OpenWRT.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: The Raspberry Pi is now a WiFi extender thanks to OpenWRT. Time to configure it.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: SSH into the Raspberry Pi and configure the WiFi settings.{player.reset}")
    task2_choice = input(f"{player.blue}Commands: [ssh root@192.168.1.1, uci set wireless.radio0.ssid='NewSSID', uci commit, wifi, abort] What will you do: {player.reset}")
    
    if "ssh root@192.168.1.1" in task2_choice.lower() and "uci set wireless.radio0.ssid='newssid'" in task2_choice.lower() and "uci commit" in task2_choice.lower() and "wifi" in task2_choice.lower():
        print(f"{player.green}You successfully SSH into the Raspberry Pi and configure the WiFi settings.{player.reset}")
        player.inventory.append("Configured Raspberry Pi")
    else:
        print(f"{player.red}Mission failed! Incorrect commands to configure the Raspberry Pi.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: With the Raspberry Pi configured, it's time to deploy it as a WiFi extender.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Secure the Raspberry Pi in a weatherproof case and throw it to a strategic location.{player.reset}")
    task3_choice = input(f"{player.blue}Commands: [secure --case, throw --location, abort] What will you do: {player.reset}")
    
    if task3_choice.lower() == "secure --case" and "throw --location" in task3_choice.lower():
        print(f"{player.green}You successfully secure the Raspberry Pi and throw it to extend your team's WiFi range. Mission accomplished!{player.reset}")
        player.inventory.append("Deployed Raspberry Pi")
    else:
        print(f"{player.red}Mission failed! You did not secure and deploy the Raspberry Pi correctly.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Creating a Portable WiFi Signal Relay' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

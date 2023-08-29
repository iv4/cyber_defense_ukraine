
import time

def run(player):
    print(f"{player.green}Mission: Setting Up a Remote Wireless Trigger Device to Destroy a Bridge{player.reset}")
    print(f"{player.yellow}Background: Intelligence reports indicate that an enemy fuel convoy is scheduled to pass over a bridge. Your mission is to set up a remote wireless trigger to destroy the bridge as the convoy passes.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in a hidden location overlooking the bridge, with your equipment beside you.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Choose the type of explosive to use.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [C-4, Dynamite, TNT, None] What type of explosive will you use: {player.reset}")
    
    if task1_choice.lower() == "c-4":
        print(f"{player.green}Excellent choice! C-4 is a stable and powerful explosive, ideal for this mission. To use C-4 in real life, you'd need a blasting cap to initiate the explosion.{player.reset}")
        player.inventory.append("C-4 Explosive")
    else:
        print(f"{player.red}Poor choice! The selected explosive is not suitable for this mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: With the explosive selected, it's time to set up the remote trigger.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Choose the triggering mechanism.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [RF Remote, Bluetooth, Wi-Fi, None] Choose your triggering mechanism: {player.reset}")
    
    if task2_choice.lower() == "rf remote":
        print(f"{player.green}Great choice! An RF remote offers a reliable and secure way to trigger the explosive. In real-life, you'd use an RF transmitter and receiver connected to a microcontroller to set up the trigger.{player.reset}")
        player.inventory.append("RF Remote Trigger")
    else:
        print(f"{player.red}Bad choice! The selected triggering mechanism is not reliable. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: You've set up the explosive and the trigger. Now, you're waiting for the enemy convoy to approach the bridge.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Trigger the explosive as the enemy convoy passes over the bridge.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [Activate, Deactivate, Do Nothing, Run Away] What will you do: {player.reset}")
    
    if task3_choice.lower() == "activate":
        print(f"{player.green}Mission accomplished! You've successfully destroyed the bridge and halted the enemy convoy. In a real-world scenario, you'd use an RF remote to send a signal to the receiver connected to the microcontroller, which would then initiate the blasting cap to explode the C-4. {player.reset}")
        player.inventory.append("Mission Accomplished Badge")
    else:
        print(f"{player.red}Mission failed! The convoy passed safely. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Setting Up a Remote Wireless Trigger Device to Destroy a Bridge' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

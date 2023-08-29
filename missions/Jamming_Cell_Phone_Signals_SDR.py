
import time

def run(player):
    print(f"{player.green}Mission: Jamming Cell Phone Signals to Prevent Remote Mine Detonation using SDR{player.reset}")
    print(f"{player.yellow}Background: You are in hostile territory, and intelligence suggests that a remote cell phone-triggered mine is planted on your escape route. Your mission is to use an SDR to jam cell phone signals and prevent its detonation.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in a makeshift camp with your team, preparing to leave. Your tech equipment, including an SDR, is laid out in front of you.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Identify the frequency range used by most cell phones.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [700-2700 MHz, 10-100 MHz, 300-400 MHz, 5000-6000 MHz] What is the correct frequency range: {player.reset}")
    
    if task1_choice.lower() == "700-2700 mhz":
        print(f"{player.green}Correct! You configure your SDR to this frequency range. To do this in real life, you'd use software like GNU Radio to set the frequency range on your SDR.{player.reset}")
        player.inventory.append("Frequency Range Info")
    else:
        print(f"{player.red}Incorrect choice. You've set the wrong frequency, compromising the mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: With the frequency range set on your SDR, it's time to test the device.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Perform a test jamming operation.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [Run Test, Skip Test, Calibrate, None] What will you do: {player.reset}")
    
    if task2_choice.lower() == "run test":
        print(f"{player.green}Excellent choice! You successfully perform a test jamming operation using your SDR and GNU Radio. Now you know the device is working as expected.{player.reset}")
        player.inventory.append("SDR Test Successful")
    else:
        print(f"{player.red}Wrong choice! You've skipped an essential step, compromising the mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: You're approaching the suspected area where the remote mine is planted. It's time to activate your SDR jammer.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Activate the SDR Jammer.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [Activate, Deactivate, Do Nothing, Throw Away] What will you do: {player.reset}")
    
    if task3_choice.lower() == "activate":
        print(f"{player.green}Good move! You've successfully jammed the cell phone signal using your SDR and GNU Radio, preventing the mine from detonating. {player.reset}")
        player.inventory.append("Activated SDR Jammer")
    else:
        print(f"{player.red}Poor decision! You've failed to jam the cell phone signal, compromising the mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Jamming Cell Phone Signals to Prevent Remote Mine Detonation using SDR' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

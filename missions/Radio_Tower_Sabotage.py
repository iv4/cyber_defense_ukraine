
import time

def run(player):
    print(f"{player.green}Mission: Radio Tower Sabotage{player.reset}")
    print(f"{player.yellow}Background: The enemy is using a local radio tower to coordinate attacks. Your mission is to disrupt their operations.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You are near the enemy radio tower and need to find a way to access its control system.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: You spot a guard near the entrance. What social engineering tactic will you use to gain entry?{player.reset}")
    task1_choice = input(f"{player.blue}Options: [Impersonate a Technician, Fake Emergency, Bribery, Distraction] Choose your tactic: {player.reset}")
    
    if task1_choice.lower() == "impersonate a technician":
        print(f"{player.green}Excellent choice! You successfully trick the guard and gain entry.{player.reset}")
        player.inventory.append("Initial Access")
    else:
        print(f"{player.red}Your tactic failed. The guard is suspicious. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: You've identified network vulnerabilities and now need to exploit them.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Choose an exploit from Metasploit to gain control over the radio tower's system.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [exploit/windows/smb/psexec, exploit/multi/handler, exploit/unix/webapp/phpmyadmin, exploit/multi/http/jboss_maindeployer] Choose your exploit: {player.reset}")
    
    if task2_choice.lower() == "exploit/windows/smb/psexec":
        print(f"{player.green}Exploit successful! You now have control over the radio tower's system.{player.reset}")
        player.inventory.append("System Control")
    else:
        print(f"{player.red}Exploit failed! Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: You have control and need to change the frequency to disrupt enemy communications.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: What Linux command will you use to change the radio frequency?{player.reset}")
    task3_choice = input(f"{player.blue}Enter the command: {player.reset}")
    
    if task3_choice.lower() == "iwconfig wlan0 freq 2.412G":
        print(f"{player.green}Frequency changed! Time to make your exit.{player.reset}")
    else:
        print(f"{player.red}Wrong command! Frequency remains the same. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Radio Tower Sabotage' completed successfully!{player.reset}")
    player.inventory.append("Radio Tower Sabotage Badge")


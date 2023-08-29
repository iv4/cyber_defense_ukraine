
import time

def run(player):
    print(f"{player.green}Mission: Secure Comms{player.reset}")
    print(f"{player.yellow}Background: Enemy forces have been intercepting our communications. Your mission is to secure them.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in the communication room and realize that enemy forces might be intercepting your messages.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: You need to identify the insecure communication channels immediately!{player.reset}")
    task1_choice = input(f"{player.blue}Options: [HTTP, HTTPS, SFTP, FTP] What channel do you suspect: {player.reset}")
    
    if task1_choice.lower() == "http" or task1_choice.lower() == "ftp":
        print(f"{player.green}Correct! You quickly switch off the insecure channels.{player.reset}")
        player.inventory.append("Intercepted Message")
    else:
        print(f"{player.red}You've failed to identify the insecure channel, compromising the mission!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: Now that the insecure channels are off, it's time to secure your own comms.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Choose an encryption algorithm for secure communication.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [AES, DES, RSA, None] What encryption will you use: {player.reset}")
    
    if task2_choice.lower() == "aes" or task2_choice.lower() == "rsa":
        print(f"{player.green}Excellent choice! Your comms are now encrypted.{player.reset}")
        player.inventory.append("Encryption Key")
    else:
        print(f"{player.red}Poor choice! You've compromised the mission!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: With your comms secure, it's time to send a crucial message to HQ.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: What command will you use to encrypt your message?{player.reset}")
    task3_choice = input(f"{player.blue}Enter the command: {player.reset}")
    
    if task3_choice.lower() == "openssl aes-256-cbc -a -salt -in message.txt -out encrypted.txt" or        task3_choice.lower() == "openssl rsa -in message.txt -out encrypted.txt":
        print(f"{player.green}Message sent! Your encrypted message is on its way to HQ.{player.reset}")
    else:
        print(f"{player.red}Command failed! The mission is compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Secure Comms' completed successfully!{player.reset}")
    player.inventory.append("Secure Comms Badge")

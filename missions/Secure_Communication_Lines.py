
import time

def run(player):
    print(f"{player.green}Mission: Secure Communication Lines{player.reset}")
    print(f"{player.yellow}Background: Enemy forces are trying to intercept your secure communications. Your mission is to secure the communication lines and prevent eavesdropping.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You are in the secure communication center where you have access to the encryption system.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: What encryption algorithm will you use to secure the communications?{player.reset}")
    task1_choice = input(f"{player.blue}Options: [AES, RSA, DES, None] Choose your algorithm: {player.reset}")
    
    if task1_choice.lower() == "aes":
        print(f"{player.green}Great choice! You successfully encrypt the communication lines.{player.reset}")
        player.inventory.append("Encryption Algorithm")
    else:
        print(f"{player.red}You failed to encrypt the lines. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: You've encrypted the lines, but you suspect there might be a mole in your team.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: How will you verify the identity of the people communicating over the line?{player.reset}")
    task2_choice = input(f"{player.blue}Options: [2FA, Fingerprint, Passphrase, None] Choose your method: {player.reset}")
    
    if task2_choice.lower() == "2fa":
        print(f"{player.green}Smart move! You've added an extra layer of security.{player.reset}")
        player.inventory.append("Identity Verification")
    else:
        print(f"{player.red}Verification failed! The mole is still at large. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: You've secured the line and verified identities. Now, you need to send a crucial message to the headquarters.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: What command will you use to send the encrypted message?{player.reset}")
    task3_choice = input(f"{player.blue}Enter the command: {player.reset}")
    
    if task3_choice.lower() == "openssl aes-256-cbc -a -salt -in message.txt -out encrypted.txt":
        print(f"{player.green}Message sent securely! Your mission is accomplished.{player.reset}")
    else:
        print(f"{player.red}Command failed! The crucial message is intercepted. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Secure Communication Lines' completed successfully!{player.reset}")
    player.inventory.append("Communication Security Badge")


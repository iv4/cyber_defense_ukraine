
import time

def run(player):
    print(f"{player.green}Mission: Frequency Hopping{player.reset}")
    print(f"{player.yellow}Background: Your mission is to prevent enemy signal interception by implementing frequency hopping.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You are in the secure communications room with access to signal modulators.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: What type of frequency hopping will you implement?{player.reset}")
    task1_choice = input(f"{player.blue}Options: [FHSS, DSSS, AFH, None] Choose your hopping method: {player.reset}")
    
    if task1_choice.lower() == "fhss":
        print(f"{player.green}Great choice! Frequency-Hopping Spread Spectrum (FHSS) is effective for avoiding signal jamming and interception.{player.reset}")
        player.inventory.append("FHSS Method")
    else:
        print(f"{player.red}Incorrect choice! The communication signals are still vulnerable. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: You've implemented FHSS. Now you need to set the hopping sequence.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: What will be your hopping sequence?{player.reset}")
    task2_choice = input(f"{player.blue}Enter a sequence of frequencies (e.g., 2.4GHz, 2.5GHz, 2.6GHz): {player.reset}")
    
    if "2.4GHz" in task2_choice and "2.5GHz" in task2_choice:
        print(f"{player.green}Good sequence! This will make it difficult for the enemy to intercept the signals.{player.reset}")
        player.inventory.append("Hopping Sequence")
    else:
        print(f"{player.red}Poor sequence! The signals are still easy to intercept. Mission compromised!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: The frequency hopping is in place. Now you need to secure the hopping codes.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: What method will you use to secure the hopping codes?{player.reset}")
    task3_choice = input(f"{player.blue}Options: [AES Encryption, RSA Encryption, Plaintext, None] Choose your method: {player.reset}")
    
    if task3_choice.lower() == "aes encryption":
        print(f"{player.green}Excellent! The hopping codes are securely encrypted. Mission successful.{player.reset}")
    else:
        print(f"{player.red}Incorrect method! The hopping codes are compromised. Mission failed!{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Frequency Hopping' completed successfully!{player.reset}")
    player.inventory.append("Frequency Hopping Badge")


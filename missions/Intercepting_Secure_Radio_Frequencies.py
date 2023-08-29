
import time

def run(player):
    print(f"{player.green}Mission: Intercepting Secure Radio Frequencies - Refined{player.reset}")
    print(f"{player.yellow}Background: Your mission is to intercept secure radio frequencies to gather critical intelligence on enemy activities. This is a refined mission focused specifically on radio frequency interception tasks.{player.reset}")
    time.sleep(2)

    print(f"{player.yellow}Scene 1: You are in the cyber warfare operations room equipped with state-of-the-art signal interception and encryption-breaking devices.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Choose the type of radio frequency to intercept.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [HF, VHF, UHF, SHF] Choose your target frequency range: {player.reset}")
    
    if task1_choice.lower() == "uhf":
        print(f"{player.green}Excellent choice! UHF is widely used for secure military communications. Moving on to the next task.{player.reset}")
        player.inventory.append("UHF Interceptor")
    else:
        print(f"{player.red}Incorrect choice. You failed to focus on the right frequency range, compromising the mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: After choosing the right frequency range, you now need to calibrate your equipment for precise interception.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Calibrate the Software Defined Radio (SDR) for optimal performance.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [Auto, Manual, Preset, None] How will you calibrate the SDR: {player.reset}")
    
    if task2_choice.lower() == "manual":
        print(f"{player.green}Smart move! Manual calibration allows you to fine-tune the SDR settings for optimal performance. {player.reset}")
        player.inventory.append("SDR Calibration")
    else:
        print(f"{player.red}Wrong choice! Due to poor calibration, you miss the secure frequencies and compromise the mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: Your SDR is now calibrated. Your next task is to identify the encryption algorithms being used on the intercepted frequencies.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Identify the encryption algorithms.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [AES, DES, RSA, Quantum] What encryption algorithms are you identifying? {player.reset}")
    
    if "aes" in task3_choice.lower() and "rsa" in task3_choice.lower():
        print(f"{player.green}Excellent identification! You've successfully identified AES and RSA as the encryption algorithms being used. {player.reset}")
        player.inventory.append("Encryption Algorithms")
    else:
        print(f"{player.red}Incorrect identification! You fail to identify the correct encryption algorithms, compromising the mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 4: The final task is to actually decrypt one of the intercepted messages to confirm its content.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 4: Decrypt the intercepted message.{player.reset}")
    task4_choice = input(f"{player.blue}Enter the command you would use to decrypt an AES encrypted message: {player.reset}")
    
    if task4_choice.lower() == "openssl aes-256-cbc -d -a -in encrypted.txt -out decrypted.txt":
        print(f"{player.green}Perfect! You've successfully decrypted the message and gathered critical intelligence. Mission complete! {player.reset}")
        player.inventory.append("Decrypted Message")
    else:
        print(f"{player.red}Wrong command! You fail to decrypt the message, compromising the mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Intercepting Secure Radio Frequencies - Refined' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")


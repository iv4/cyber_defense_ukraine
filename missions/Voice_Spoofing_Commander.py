
import time

def run(player):
    print(f"{player.green}Mission: Spoofing an Enemy Commander's Voice{player.reset}")
    print(f"{player.yellow}Background: Your task is to use Descript's Overdub software to impersonate an enemy commander's voice to sow confusion.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You're in a makeshift studio with all the required software and audio equipment.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Gather voice samples of the enemy commander using Audacity.{player.reset}")
    task1_choice = input(f"{player.blue}Commands: [audacity --record, audacity --skip, abort] What will you do: {player.reset}")
    
    if task1_choice.lower() == "audacity --record":
        print(f"{player.green}You successfully gather voice samples using Audacity without arousing suspicion. The samples are sufficient for Descript's Overdub.{player.reset}")
        player.inventory.append("Voice Samples")
    else:
        print(f"{player.red}Mission failed! You can't proceed without the voice samples.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: With the voice samples, you're now ready to create the deepfake audio using Descript's Overdub.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Generate the deepfake audio using Descript's Overdub.{player.reset}")
    task2_choice = input(f"{player.blue}Commands: [overdub --generate, overdub --skip, abort] What will you do: {player.reset}")
    
    if task2_choice.lower() == "overdub --generate":
        print(f"{player.green}You use Descript's Overdub to generate a deepfake audio that mimics the enemy commander's voice.{player.reset}")
        player.inventory.append("Deepfake Audio")
    else:
        print(f"{player.red}Mission failed! Without the deepfake audio, you can't proceed.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: You are ready to transmit the deepfake audio, but you notice that enemy forces are getting suspicious. It's a close call!{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Transmit the deepfake audio without getting caught using VLC media player.{player.reset}")
    task3_choice = input(f"{player.blue}Commands: [vlc --transmit, vlc --delay, abort] What will you do: {player.reset}")
    
    if task3_choice.lower() == "vlc --transmit":
        print(f"{player.green}You successfully transmit the deepfake audio using VLC, causing confusion in the enemy camp. The mission is complete!{player.reset}")
        player.inventory.append("Successful Transmission")
    elif task3_choice.lower() == "vlc --delay":
        print(f"{player.green}Smart move! You delay the transmission using VLC until suspicion dies down and then successfully transmit the deepfake audio. The mission is complete!{player.reset}")
        player.inventory.append("Delayed but Successful Transmission")
    else:
        print(f"{player.red}Mission failed! Without transmitting the audio, the mission is incomplete.{player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Spoofing an Enemy Commander's Voice' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")

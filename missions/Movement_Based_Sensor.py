
import time

def run(player):
    print(f"{player.green}Mission: Setting Up a Movement-Based Sensor{player.reset}")
    print(f"{player.yellow}Background: Your team needs to secure a location that is suspected to be frequented by enemy agents. Your mission is to set up a movement-based sensor to detect any unauthorized entry.{player.reset}")
    time.sleep(2)
    
    print(f"{player.yellow}Scene 1: You've reached the location and are ready to deploy the sensor.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 1: Choose the type of sensor to use.{player.reset}")
    task1_choice = input(f"{player.blue}Options: [PIR, Ultrasonic, Lidar, None] What type of sensor will you use: {player.reset}")
    
    if task1_choice.lower() == "pir":
        print(f"{player.green}Excellent choice! A Passive Infrared (PIR) sensor detects changes in thermal energy, making it ideal for detecting human movement. To set it up, you'd connect it to a microcontroller and configure the sensitivity settings.{player.reset}")
        player.inventory.append("PIR Sensor")
    else:
        print(f"{player.red}Poor choice! The selected sensor is not suitable for this mission. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 2: With the sensor chosen, it's time to position it effectively.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 2: Choose the optimal position for the sensor.{player.reset}")
    task2_choice = input(f"{player.blue}Options: [Doorway, Window, Ceiling, None] Where will you place the sensor: {player.reset}")
    
    if task2_choice.lower() == "doorway":
        print(f"{player.green}Great choice! Placing the sensor at the doorway maximizes the chances of detecting any unauthorized entry. In a real-world scenario, you'd ensure the sensor has a clear line of sight to the entry point.{player.reset}")
        player.inventory.append("Optimal Sensor Position")
    else:
        print(f"{player.red}Bad choice! The selected position is not optimal for detecting movement. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.yellow}Scene 3: The sensor is set up and operational. You are monitoring the sensor data remotely.{player.reset}")
    time.sleep(2)
    print(f"{player.blue}Task 3: Analyze the sensor data to identify any unauthorized entry.{player.reset}")
    task3_choice = input(f"{player.blue}Options: [Investigate, Ignore, Disable, None] The sensor has detected movement, what will you do: {player.reset}")
    
    if task3_choice.lower() == "investigate":
        print(f"{player.green}Mission accomplished! You've successfully detected unauthorized entry and alerted your team. In a real-world scenario, the PIR sensor would be configured to send alerts to a monitoring system or smartphone app.{player.reset}")
        player.inventory.append("Mission Accomplished Badge")
    else:
        print(f"{player.red}Mission failed! You missed the unauthorized entry. {player.reset}")
        return

    time.sleep(2)
    print(f"{player.green}Congratulations! Mission 'Setting Up a Movement-Based Sensor' completed successfully!{player.reset}")
    player.inventory.append("Mission Completion Badge")


from colorama import Fore, Style, init
import os
import glob
import importlib
import time

# Initialize colorama
init(autoreset=True)

# Ukrainian and Cyber warfare colors
blue = Fore.BLUE
yellow = Fore.YELLOW
green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL

class CyberRPG:
    def __init__(self):
        init(autoreset=True)

        self.blue = Fore.BLUE
        self.yellow = Fore.YELLOW
        self.green = Fore.GREEN  # add this line
        self.red = Fore.RED
        self.reset = Style.RESET_ALL
        
        # Ukrainian and Cyber warfare colors
        blue = Fore.BLUE
        yellow = Fore.YELLOW
        green = Fore.GREEN
        white = Fore.WHITE
        red = Fore.RED
        reset = Style.RESET_ALL

        print(blue + "|Welcome to Cyber Defense Ukraine|")
        time.sleep(2)
        print(blue + "|===An Electronic Warfare RPG====|")
        time.sleep(2)
        print(yellow + "|!!!!!!!!!!SLAVA_UKRAINE!!!!!!!!!|")
        print(yellow + "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|")
        time.sleep(2)
        print("\n")
        print(blue + "Created by milosilo")
        print(yellow + "https://github.com/milosilo")
        time.sleep(2)
        print("\n")
        print(red + "On Thursday, Feb 24, 2022, Russia Invaded the Sovereign nation of Ukraine. They thought it would be easy...")
        time.sleep(2)
        print(blue + "The Ukrainian Cyber Warfare Operations Task Force you are apart of has been sent to sow sunflower seeds")
        time.sleep(2)
        print("Your Task and Purpose is to defend your nation by using sophistcated cyber warfare TTPs against the Russian aggressors")
        time.sleep(2)
        print("\n")
        
        
        self.current_city = "Kyiv"
        self.inventory = []
        self.load_missions()

    def load_missions(self):
        self.missions = {}
        mission_files = glob.glob("missions/*.py")
        for mission_file in mission_files:
            mission_name = os.path.basename(mission_file)[:-3]
            mission_module = importlib.import_module(f"missions.{mission_name}")
            self.missions[mission_name] = mission_module

    def start_game(self):
        while True:
            print(f"{yellow}Current city: {self.current_city}{reset}")
            print(f"{green}1. Start a mission{reset}")
            print(f"{red}2. View inventory{reset}")
            print(f"{green}3. Move to another city{reset}")
            print(f"{red}4. Exit game{reset}")

            choice = input(f"{blue}Choose an option: {reset}")

            try:
                if int(choice) in range(1, 5):
                    if choice == "1":
                        self.start_mission()
                    elif choice == "2":
                        self.view_inventory()
                    elif choice == "3":
                        self.move_city()
                    elif choice == "4":
                        print(f"{red}Exiting game.{reset}")
                        break
                else:
                    print(f"{red}Invalid choice. Please try again.{reset}")
            except ValueError:
                print(f"{red}Please enter a number.{reset}")

    def start_mission(self):
        while True:
            print(f"{yellow}Available missions in {self.current_city}:{reset}")
            for idx, mission in enumerate(self.missions):
                print(f"{idx + 1}. {mission}")
            print(f"{red}5. Go back to city menu{reset}")
            
            mission_choice = input(f"{blue}Choose a mission or go back to city menu: {reset}")
            
            if mission_choice == "5":
                print(f"{green}Going back to city menu.{reset}")
                break

            try:
                if int(mission_choice) in range(1, len(self.missions) + 1):
                    selected_mission = list(self.missions.keys())[int(mission_choice) - 1]
                    self.missions[selected_mission].run(self)
                else:
                    print(f"{red}Invalid choice. Please try again.{reset}")
            except ValueError:
                print(f"{red}Please enter a number.{reset}")

    def view_inventory(self):
        print(f"{green}Your inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}{reset}")

    def move_city(self):
        available_cities = ["Kyiv", "Lviv", "Odessa", "Dnipro", "Kharkiv"]
        print(f"{yellow}Available cities: {', '.join(available_cities)}{reset}")
        new_city = input(f"{blue}Choose a city to move to: {reset}")
        if new_city in available_cities:
            self.current_city = new_city
            print(f"{green}You have moved to {new_city}.{reset}")
        else:
            print(f"{red}Invalid city. Please try again.{reset}")

if __name__ == "__main__":
    game = CyberRPG()
    game.start_game()

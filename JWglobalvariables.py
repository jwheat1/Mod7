import random

# Class for managing player details
class Player:
    def __init__(self, name, health, equipment, location):
        self.name = name
        self.health = health
        self.equipment = equipment  # List of items the player carries
        self.location = location  # Current location in the station

    def get_health(self):
        return self.health
    
    def update_health(self, value):
        self.health += value

    def get_equipment(self):
        return self.equipment

    def add_equipment(self, item):
        self.equipment.append(item)

    def set_location(self, new_location):
        self.location = new_location

# Class for managing the Creature (Alien) encounters
class Creature:
    def __init__(self, species, health, behavior):
        self.species = species
        self.health = health
        self.behavior = behavior  # How the creature acts (hostile, passive, etc.)
    
    def get_health(self):
        return self.health

    def update_health(self, damage):
        self.health -= damage

# Initialize the player character
player = Player("Engineer", 100, [], "Docking Bay")  # Default player details

# Initialize the first encountered creature (Alien)
creature = Creature("Unknown Alien", 50, "Hostile")

# Game-related global variables
game_state = {
    'hasDataLog': False,  # If player has accessed the lab data log
    'hasCreatureData': False,  # If player has learned the creature's backstory
    'hasControlRoomKey': False,  # If the player has the control room access code
    'hasBackupPowerCell': False,  # If the player has found the backup power cell
    'current_chapter': 1,  # Tracks which chapter the player is currently in
    'game_won': False,  # Whether the player has completed the game
    'game_ended': False,  # Whether the game has ended
}

# Locations within the station (for reference)
locations = {
    "Docking Bay": "A cold and quiet docking bay, you hear distant hums.",
    "Main Hallway": "A long, dimly lit hallway stretching into darkness.",
    "Laboratory": "A lab filled with overturned equipment and strange devices.",
    "Greenhouse": "A greenhouse with bizarre alien plant life.",
    "Control Room": "The station's nerve center, locked and requiring access.",
}

# Possible endings based on player choices
victory_choices = ["send_report", "delete_data", "shut_down_station"]
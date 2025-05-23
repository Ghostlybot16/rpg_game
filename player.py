from combatant import Combatant

class Player(Combatant):
    """
    A class to create a player.
    
    Args:
        name (str): The player's name
        attack_name (str): The name of the attack the player uses
        attack_power (int): The power value of the player's attack
        defense (int): The value of the player's defense
        inventory (dict): The player's inventory 
    """
    
    def __init__(self, name: str, attack_name: str ,attack_power: int, defense: int, inventory: dict):
        """Initializes a new Player instance with protected attributes"""
        self.name = name
        self._max_health = 100
        self._health = self._max_health
        self._attack_name = attack_name.upper()
        self._attack_power = attack_power 
        self._defense = defense
        self._inventory = inventory
    
    
    # Player attacks an enemy
    def attacks(self, enemy: Combatant) -> None:
        """
        Outputs the attack scenario by mentioning the attack name and who the attack is being used against 
        
        Args:
            enemy (Combatant): The enemy player who is receiving the attack (attack_name)
        """
        if enemy.is_defeated(): # Prevents attacking an already dead combatant
            print(f"--- Stop it {enemy.name} is already dead! ---\n")
            return

        print(f"{self.name} used {self._attack_name} on {enemy.name}\n")
        enemy.take_damage(self._attack_power)
    
    
    # Health gets reduced when attacked
    def take_damage(self, amount: int) -> None:
        """
        Outputs a message to communicate that a player has taken damage & Outputs the updated DECREASED health

        Args:
            amount (int): Integer amount of the value of the damage that is going to be done
        """
        self._health -= amount

        if self._health <= 0:
            self._health = 0

        print(f"--- {self.name} TOOK DAMAGE! ---")
        print(f"{self.name}'s health is now: {self._health}\n")
        
    
    # Restore health 
    def heal(self, amount: int) -> None:
        """
        Communicates via a message that a player has been healed by the provided 'amount'
        Outputs the updated INCREASED health
        Heals the player's health up to their maximum health limit.

        Args:
            amount (int): The amount of health that is going to be restored to the player's health
        """
        self._health = min(self._health + amount, self._max_health)
        print(f"--- {self.name} HEALED ---")
        print(f"{self.name} health: {self._health} \n")


    # Predicate method (Method to check a condition, returns a bool value)
    def is_defeated(self) -> bool:
        """
        Checks if the player's health has reached 0 or below

        Returns:
            bool: True is the player has been defeated, False otherwise

        """
        return self._health <= 0

    @property # Getter Method
    def inventory(self) -> dict:
        """
        Gets a copy of the player's current inventory

        Returns:
            dict: A copy of the inventory with item names and their quantity

        """
        return self._inventory.copy()

    @property
    def health(self) -> int:
        """
        Gets the current health of the player

        Returns:
            int: The current health value of the player

        """
        return self._health

    @property
    def max_health(self) -> int:
        """
        Gets the maximum health of the player

        Returns:
            int: The maximum health value of the player.
        """
        return self._max_health

    def add_to_inventory(self, new_item: str, quantity_of_item: int = 1) -> None:
        """
        Checks if a new item already exists within the player's inventory. 
        If yes, increase the item's max quantity.
        If no, add the new item with the provided quantity (defaults of 1 for new items).

        This method also gets triggered when player tries to add a dropped item (after enemy defeat) to their inventory.

        Args:
            new_item (str): New item that the player comes across
            quantity_of_item (int, optional): The number of times the item is added to the player's inventory after dropped from defeated enemy or picked up
        """
        if new_item in self._inventory: # Check if the new item already exists within the player's inventory. If yes, increase its quantity
            self._inventory[new_item] += quantity_of_item
        else:
            self._inventory[new_item] = quantity_of_item # If new item doesn't exist in inventory, Add the new item and default its value to 1

        print(f"{new_item} x{quantity_of_item} added to {self.name}'s inventory.\n")
    
    def show_inventory(self) -> None:
        """
        Outputs the inventory items of the player. In the format "--> [item_name] x[item_quantity]"
        
        The method checks if the inventory is empty. If yes, print out an empty inventory message. If no, show the inventory items

        Returns:
            dict: The list of items returned from the players inventory
        """
        print(f"{self.name}'s INVENTORY:") # Header of the inventory view
        
        if len(self._inventory) == 0:
            print(f"(Empty Inventory)")

        else:
            for all_items in self._inventory:
                print(f"--> {all_items} x{self._inventory[all_items]}\n")
        

    def collect_loot(self, enemy: Combatant) -> None:
        """
        Collects loot dropped from a defeated enemy and adds it to the player's inventory.

        Args:
            enemy (Combatant): The enemy which drops loot.
        """
        dropped_loot = enemy.drop_loot() # Enemy's dropped loot

        if not dropped_loot:
            print("No dropped loot to collect.")
            return

        print(f"{self.name} collected loot from {enemy.name}.\n") # Loot collected output message

        for dropped_item, quantity in dropped_loot.items():
            self.add_to_inventory(dropped_item, quantity)



# Using keyword argument during object creation for better readability
player1 = Player(
    name="Kramptj",
    attack_name="Punch", 
    attack_power=10, 
    defense=10, 
    inventory={ "Potion": 2 } # Every player gets 2 potions by default upon creation
) 

enemy1 = Player(
    name="Bertha",
    attack_name="Kick", 
    attack_power=10, 
    defense=10, 
    inventory={ "Potion": 2 })

player2 = Player(
    name="Bob",
    attack_name="Push",
    attack_power=15,
    defense=8,
    inventory={} # Testing empty inventory output
)

if __name__ == "__main__":

    player1.attacks(enemy1)
    enemy1.attacks(player1)

    player1.heal(10)
    enemy1.heal(10)

    player1.take_damage(3)

    player1.show_inventory()
    enemy1.show_inventory()
    player2.show_inventory()

    
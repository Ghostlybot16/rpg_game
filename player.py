class Player():
    """
    A class to create a player.
    
    Attributes:
        name (str): The player's name
        health (int): The player's total health
        attack_name (str): The name of the attack the player uses
        attack_power (int): The power value of the player's attack
        defese (int): The value of the player's defense 
        inventory (dict): The player's inventory 
    """
    
    def __init__(self, name: str, health: int, attack_name: str ,attack_power: int, defense: int, inventory: dict):
        """Initializes a new Player instance with protected attributes"""
        self.name = name
        self._health = health
        self._attack_name = attack_name.upper()
        self._attack_power = attack_power 
        self._defense = defense
        self._inventory = inventory
    
    
    # Player attacks an enemy
    def attacks(self, enemy: object):
        """
        Outputs the attack scenario by mentioning the attack name and who the attack is being used against 
        
        Args:
            enemy (object): The enemy player who is receiving the attack (attack_name)
        """
        print(f"{self.name} used {self._attack_name} on {enemy.name}\n")
        enemy.take_damage(self._attack_power)
    
    
    # Health gets reduced when attacked
    def take_damage(self, amount: int) -> str:
        """
        Outputs a message to communicate that a player has taken damage & Outputs the updated DECREASED health

        Args:
            amount (int): Integer amount of the value of the damage that is going to be done
        """
        self._health -= amount
        print(f"{self.name} TOOK DAMAGE!")
        print(f"{self.name}'s health is now: {self._health}\n")
        
    
    # Restore health 
    def heal(self, amount: int) -> str:
        """
        Outputs a message to communicate that a player has healed by the provided amount & Outputs the updated INCREASED health

        Args:
            amount (int): _description_
        """
        self._health += amount
        print(f"{self.name} HEALED")
        print(f"{self.name} health: {self._health} \n")
    
    def add_to_inventory(self, new_item: str) -> str:
        """
        Checks if a new item already exists within the player's inventory. 
        If yes, increase the item's max quanity. 
        If no, add the new item and set it's value to 1.

        Args:
            new_item (str): New item that the player comes across
        
        Returns:
            str: A message communicating that the item has been added to the player's inventory
        """
        if new_item in self._inventory: # Check if the new item already exists within the player's inventory. If yes, increase it's quantity
            self._inventory[new_item] += 1 
        else:
            self._inventory[new_item] = 1 # If new item doesn't exist in inventory, Add the new item and default it's value to 1 
        
        print(f"{new_item} added to {self.name}'s Inventory.\n")
    
    def show_inventory(self) -> dict:
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
        
    
# Using keyword argument during object creation for better readability
player1 = Player(
    name="Kramptj", 
    health=100, 
    attack_name="Punch", 
    attack_power=10, 
    defense=10, 
    inventory={ "Potion": 2 } # Every player gets 2 potions by default upon creation
) 

enemy1 = Player(
    name="Bertha", 
    health=100, 
    attack_name="Kick", 
    attack_power=10, 
    defense=10, 
    inventory={ "Potion": 2 })

player2 = Player(
    name="Bob",
    health=80,
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

    
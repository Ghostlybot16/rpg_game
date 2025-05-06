from combatant import Combatant

class Enemy(Combatant):
    """
    A class to create an enemy.
    
    Args:
        name (str): The enemy's name
        health (int): The enemy's health
        max_health(int): The enemy's maximum health
        attack_name (str): The name of the enemy's attack
        attack_power(int): The power of the enemy's attack
        defense (int): The value of the enemy's defense 
        inventory (dict): The enemy's inventory (The Item that is dropped upon the enemy's defeat)
    """
    def __init__(self, name: str, health: int, max_health: int, attack_name: str, attack_power: int, defense: int, inventory: dict):
        """Initializes a new Enemy instance with protected attributes"""
        self.name = name
        self._health = health
        self._max_health = max_health
        self._attack_name = attack_name.upper()
        self._attack_power = attack_power
        self._defense = defense
        self._inventory = inventory

    # Getter methods
    @property
    def inventory(self) -> dict:
        return self._inventory

    @property
    def health(self) -> int:
        return self._health

    @property
    def max_health(self) -> int:
        return self._max_health

    # Enemy attack back to player
    def attacks(self, target: Combatant) -> None:
        """
        Outputs the attack scenario by mentioning the attack name, who the attack is being used against 
        and calls the take_damage method to lower the opponents max health.

        Args:
            target (Combatant): The combatant (Player) who is receiving the damage from the enemy
        """
        if target.is_defeated():
            print(f"{target.name} is already defeated!")
            return

        print(f"--- {self.name} attacks back with {self._attack_name} to {target.name}! ---\n")
        target.take_damage(self._attack_power)
    
    
    # Players health gets reduced by enemy 
    def take_damage(self, amount: int) -> None:
        """
        The method that is called to reduce the target's health by the given amount.
        This method also checks if the health has been lowered to a negative amount, if yes, then set it to 0

        Args:
            amount (int): The amount of health to be lowered. It is the attack_power value.

        Returns:
            str: The message communicating that the target took damage & Outputs the new lowered health value
        """
        self._health -= amount

        if self._health < 0: # Check if enemy health dropped below 0 after taking damage. If yes, health = 0
            self._health = 0
            
        print(f"--- {self.name} TOOK DAMAGE! ---")
        print(f"{self.name}'s new health: {self._health}")
        print("------------------------------")


    # Predicate method (Method to check a condition, returns a bool value)
    def is_defeated(self) -> bool:
        """
        Checks if the enemy's health has reached 0 or below

        Returns:
            bool: True if the enemy is defeated, False otherwise

        """
        return self._health <= 0

    def drop_loot(self) -> dict:
        """
        Enemy drops loot once they are defeated by a player and Enemy's inventory is emptied once loot has been dropped.

        Returns:
            dict: If enemy has been successfully defeated, the player receives the dropped items
        """
        if self.is_defeated():
            print(f"--- {self.name} DEFEATED! ---")
            print(f"Dropped Items: {self._inventory}\n")

            dropped_items = self._inventory.copy() # Copy the items to another variable
            self._inventory = {} # Clear out enemy inventory after loot drop
            return dropped_items
        else:
            print(f"{self.name} is still alive! No loot to drop.\n")
            return {}
            
    
# Object Creation using keyword arguments 
goblin = Enemy(
    name="Goblin",
    health=50,
    max_health=50,
    attack_name="Rusty Shiv",
    attack_power=5,
    defense=5,
    inventory={ "Gold Coin": 1 }
)

testPlayer = Enemy(
    name="Beep",
    health=50,
    max_health=50,
    attack_name="Shove",
    attack_power=6,
    defense=8,
    inventory={ "Potion": 2 }
)
    
if __name__ == "__main__":
   
    # Test attack method
    goblin.attacks(testPlayer)
    
    # Test loot drop
    goblin.take_damage(100) # Force goblin to 0 hp
    loot = goblin.drop_loot()
    print(f"Collected loot: {loot}")
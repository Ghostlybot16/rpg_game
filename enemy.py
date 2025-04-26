class Enemy():
    """
    A class to create an enemy.
    
    Attributes:
        name (str): The enemy's name
        health (int): The enemy's total health
        attack_name (str): The name of the enemy's attack 
        defense (int): The value of the enemy's defense 
        inventory (dict): The enemy's inventory (The Item that is dropped upon the enemy's defeat)
    """
    def __init__(self, name: str, health: int, attack_name: str, attack_power: int, defense: int, inventory: dict):
        """Initializes a new Enemy instance with protected attributes"""
        self.name = name
        self._health = health
        self._attack_name = attack_name.upper()
        self._attack_power = attack_power
        self._defense = defense
        self._inventory = inventory
    
    # Enemy attack back to player
    def attacks(self, target: object) -> str:
        """
        Outputs the attack scenario by mentioning the attack name, who the attack is being used against 
        and calls the take_damage method to lower the opponents max health.

        Args:
            target (object): The object (Player) who is receiving the damage from the enemy 
        """
        print(f"{self.name} attacks back with {self._attack_name} to {target.name}!\n")
        target.take_damage(self._attack_power)
    
    
    # Players health gets reduced by enemy 
    def take_damage(self, amount: int) -> str:
        """
        The method that is called to reduce the target's health by the given amount.
        This method also checks if the health has been lowered to a negative amount, if yes, then set it to 0

        Args:
            amount (int): The amount of health to be lowered. It is the attack_power value.

        Returns:
            str: The message communicating that the target took damage & Outputs the new lowered health value
        """
        self._health -= amount
        if self._health < 0:
            self._health = 0
            
        print(f"{self.name} TOOK DAMAGE!")
        print(f"{self.name}'s new health: {self._health}")
        print("------------------------------")
    
    def drop_loot(self):
        """
        Enemy drops loot once they are defeated by a player. 

        Returns:
            dict: If enemy has been successfully defeated, the player recieve the dropped items 
        """
        if self._health <= 0:
            print(f"{self.name} DEFEATED!")
            print(f"Dropped Items: {self._inventory}\n")
            return self._inventory
        else:
            print(f"{self.name} is still alive! No loot to drop.\n")
            return {}
            
    
# Object Creation using keyword arguments 
goblin = Enemy(
    name="Goblin",
    health=50,
    attack_name="Rusty Shiv",
    attack_power=5,
    defense=5,
    inventory={ "Gold Coin": 1 }
)

testPlayer = Enemy(
    name="Beep",
    health=50,
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
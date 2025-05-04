import unittest
from player import Player
from enemy import Enemy

class TestPlayer(unittest.TestCase):
    pass

    def setUp(self):
        self.player = Player(
            name="TestPlayer",
            health=100,
            attack_name="Punch",
            attack_power=10,
            defense=5,
            inventory={"Potion": 2}
        )

    # Testing Healing 
    def test_heal_increases_health(self):
        self.player.heal(10) # Heal the player by 10 HP 
        self.assertEqual(self.player._health, 110) # Check if the health equals 110
        

    # Testing Taking Damage
    def test_take_damage_decreases_health(self):
        self.player.take_damage(20) # Take 20 damage 
        self.assertEqual(self.player._health, 80) # Check if the updated health decreased to 80


    # Testing Adding to Inventory (Existing Item)
    def test_add_existing_item_to_inventory(self):
        self.player.add_to_inventory("Potion") 
        self.assertEqual(self.player._inventory["Potion"], 3) # Check if the potion quantity updated to 3 


    # Testing Adding to Inventory (New Item)
    def test_add_new_item_to_inventory(self):
        self.player.add_to_inventory("Sword")
        self.assertEqual(self.player._inventory["Sword"], 1) # Check if new item added with count 1 

    # Testing empty inventory
    def test_empty_inventory(self):
        empty_inventory_player = Player(
            name="EmptyPlayer",
            health=100,
            attack_name="Kick",
            attack_power=10,
            defense=5,
            inventory={} # Empty inventory
        )
        self.assertEqual(len(empty_inventory_player._inventory), 0) # Check if inventory is empty

    def test_show_inventory_runs_without_crashing(self):
        try:
            self.player.show_inventory()
        except Exception as e:
            self.fail(f"show_inventory() crashed with exception: {e}")

    # Testing collecting loot from a defeated enemy
    def test_collect_loot_adds_items_to_inventory(self):
        enemy = Enemy(
            name="Goblin",
            health=10,
            attack_name="Stab",
            attack_power=5,
            defense=2,
            inventory={"Gold Coin": 2}
        )
        enemy.take_damage(11) # Defeat the enemy
        self.player.collect_loot(enemy)

        self.assertIn("Gold Coin", self.player._inventory)
        self.assertEqual(self.player._inventory["Gold Coin"], 2)

    # Testing enemies with no loot drop nothing
    def test_collect_loot_from_alive_enemy_does_nothing(self):
        enemy = Enemy(
            name="Alive Goblin",
            health=50,
            attack_name="Stab",
            attack_power=5,
            defense=2,
            inventory={"Gold Coin": 1}
        )
        self.player.collect_loot(enemy)
        self.assertNotIn("Gold Coin", self.player._inventory) # Should not have added anything

    # Testing to ensure loot is cleared from enemy after drop
    def test_enemy_inventory_cleared_after_loot_drop(self):
        enemy = Enemy(
            name="Goblin",
            health=10,
            attack_name="Stab",
            attack_power=5,
            defense=2,
            inventory={"Gold Coin": 1}
        )
        enemy.take_damage(15) # Defeat the enemy
        self.player.collect_loot(enemy)
        self.assertEqual(enemy._inventory, {}) # Inventory should be empty
    
if __name__ == "__main__":
    unittest.main()
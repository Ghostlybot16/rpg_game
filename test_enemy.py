import unittest
from enemy import Enemy

class TestEnemy(unittest.TestCase):
    pass

    def setUp(self):
        self.enemy = Enemy(
            name="TestGoblin",
            health=50,
            max_health=50,
            attack_name="Slash",
            attack_power=10,
            defense=5,
            inventory={ "Gold Coin": 1 }
        )
        self.target = Enemy( # Dummy enemy as a target 
            name="DummyPlayer",
            health=50,
            max_health=50,
            attack_name="Slap",
            attack_power=5,
            defense=3,
            inventory={}
        )
        
    def test_initial_health(self):
        self.assertEqual(self.enemy._health, 50) # Check if the goblins initial health is 50
    
    def test_attack_reduces_target_health(self):
        self.enemy.attacks(self.target)
        self.assertEqual(self.target._health, 40) # Check if DummyPlayer's health gets lowered to 40 after 1 attack
    
    def test_take_damage_decreases_health(self):
        self.enemy.take_damage(15)
        self.assertEqual(self.enemy._health, 35) # Check if Goblins health lowers to 35 after calling the take_damage() method 
    
    def test_health_does_not_go_negative(self):
        self.enemy.take_damage(100)
        self.assertEqual(self.enemy._health, 0) # Check if Goblin's health gets lowered to 0 after taking damage that is greater than its max health
    
    def test_drop_loot_exists(self):
        try:
            self.enemy.drop_loot()
        except Exception as e:
            self.fail(f"drop_loot() crashed with exception: {e}")

    def test_attack_does_not_affect_defeated_target(self):
        self.target.take_damage(100)
        self.enemy.attacks(self.target)
        self.assertEqual(self.target.health, 0)

    def test_is_defeated_true_when_zero_health(self):
        self.enemy.take_damage(50)
        self.assertTrue(self.enemy.is_defeated())

    def test_is_defeated_false_when_alive(self):
        self.assertFalse(self.enemy.is_defeated())

    # Check to see if the correct inventory is returned to the player after enemy death
    def test_drop_loot_when_enemy_defeated(self):
        self.enemy.take_damage(100) # Enemy health drops to 0
        
        loot = self.enemy.drop_loot()
        expected_loot = {"Gold Coin": 1}
        
        self.assertEqual(loot, expected_loot)

    # Test to check that no loot is dropped when enemy is still alive
    def test_drop_loot_when_enemy_alive(self):
        loot = self.enemy.drop_loot() # Enemy still alive 
        self.assertEqual(loot, {})

    def test_drop_loot_inventory_cleared_after_drop(self):
        self.enemy.take_damage(100)
        self.enemy.drop_loot()
        self.assertEqual(self.enemy.inventory, {})

if __name__ == "__main__":
    unittest.main()

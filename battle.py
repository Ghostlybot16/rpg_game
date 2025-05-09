from player import Player
from enemy import Enemy
import random
from typing import Sequence
"""
battle.py 

This module handles the main turn-based battle logic between a human player and an AI-controlled enemy. 
It supports player choices (attack or heal), random enemy actions, victory/defeat conditions and loot collection after enemy defeat 
"""

def battle(player: Player, enemy: Enemy) -> None:
    """
    Runs a full turn-based battle between a Player and an Enemy

    The player can choose to attack or heal each turn.
    The enemy performs random actions (currently only attack)
    The battle ends when either combatant is defeated.
    Loot is collected from Enemy if the Player wins

    Args:
        player (Player): The human-controlled player instance.
        enemy(Enemy): The AI-controlled enemy instance

    """

    print("-------------------------")
    print(f"Initiating battle...")
    print(f"{player.name}'s Health: {player.health} \n{enemy.name}'s Health: {enemy.health}") # Show initial full health of both combatants
    print("--- Battle Begins! ---")

    first_turn = True # Flag to control when to show "NEW TURN" divider

    # Loop continues until one combatant is defeated
    while not player.is_defeated() and not enemy.is_defeated():

        if not first_turn: # Show divider after first turn
            print("--- NEW TURN ---")

        while True: # Loop until valid input

            player_battle_choice = input("Choose your next move:\n1. Attack\n2. Heal\n")

            if player_battle_choice == "1":
                player.attacks(enemy)
                break
            elif player_battle_choice == "2":
                print(f"{player.name} used Potion to heal.")
                player.heal(10)
                print(f"{player.name}'s health Increased to {player.health}")
                break
            else:
                print("Invalid input. Please enter 1 or 2.")

        # Check if enemy was defeated after player's action
        if enemy.is_defeated():
            print("--- VICTORY! ---")
            print(f"{player.name} has defeated {enemy.name}!")

            player.collect_loot(enemy)
            break

        # Enemy randomly chooses and executes an action (currently just "attack")
        list_of_enemy_moves: Sequence[str] = ["attack"]
        enemy_attack_choice = random.choice(list_of_enemy_moves)
        print(f"{enemy.name} chose to {enemy_attack_choice} {player.name}")

        if enemy_attack_choice == "attack":
            enemy.attacks(player)

        # Show updated health of both combatants after their choice of action onto one another
        print(f"***** {player.name}: {player.health}HP | {enemy.name}: {enemy.health}HP *****\n")

        if player.is_defeated():
            print("--- YOU DIED, GAME OVER! ---")
            break

        first_turn = False

if __name__ == "__main__":

    test_player = Player(
        name="Kramptj",
        attack_name="Punch",
        attack_power=10,
        defense=5,
        inventory={"Potion": 2}
    )

    test_enemy = Enemy(
        name="Goblin",
        health=30,
        max_health=30,
        attack_name="Bite",
        attack_power=6,
        defense=3,
        inventory={"Gold Coin": 1}
    )

    battle(test_player, test_enemy)
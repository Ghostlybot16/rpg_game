from typing import Protocol

class Combatant(Protocol):
    """
    A Protocol that defines the basic interface for any combat-capable entity.
    such as Player and Enemy

    Any class that implements this interface must provide:
    - A 'name' attribute
    - An "attacks()" method to engage in combat with another combatant (Player or Enemy)
    - A "take_damage()" method to receive damage from a combatant

    """
    name: str

    def attacks(self, target: "Combatant") -> None:
        """
        Method that represents attacking another combatant.

        Args:
            target (Combatant): The opponent (combatant) being attacked

        """
        pass

    def take_damage(self, damage: int) -> None:
        """
        Method that applies damage to the combatant

        Args:
            damage (int): The amount of damage received
        """
        pass

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
    name: str # Name of the combatant

    def attacks(self, target: "Combatant") -> None:
        """
        Method that executes an attack on to another combatant.

        Args:
            target (Combatant): The opponent (combatant) being attacked

        """
        ...

    def take_damage(self, damage: int) -> None:
        """
        Method that applies damage to the combatant. The combatant's health drops by the 'damage' amount

        Args:
            damage (int): The amount of damage received by the combatant from an opponent
        """
        ...

    def is_defeated(self) -> bool:
        """
        Checks whether the combatant has been defeated (ex: health = 0 or below)

        Returns:
            bool: True if defeated, False otherwise

        """
        ...
import random

class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def attack(self, target):
        damage = max(1, self.attack_power - target.defense)
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name}! Deals {damage} damage.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Remaining health: {self.health}")

    def is_alive(self):
        return self.health > 0


class Warrior(Character):
    def __init__(self, name, health, attack_power, defense, speed, rage=0):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = rage

    def take_damage(self, amount):
        super().take_damage(amount)
        self.rage += amount // 2
        if self.health < (self.health * 0.3):
            self.berserk_mode()

    def berserk_mode(self):
        if self.health < (self.health * 0.3):
            self.attack_power *= 2
            print(f"{self.name} enters Berserk Mode! Attack power doubled!")


class Mage(Character):
    def __init__(self, name, health, attack_power, defense, speed, mana):
        super().__init__(name, health, attack_power, defense, speed)
        self.mana = mana

    def fireball(self, target):
        if self.mana >= 10:
            damage = self.attack_power + 10
            self.mana -= 10
            self.health -= 5
            target.take_damage(damage)
            print(f"{self.name} casts Fireball on {target.name}! Deals {damage} damage but loses 5 health.")
        else:
            print(f"{self.name} doesn't have enough mana to cast Fireball!")


class Archer(Character):
    def __init__(self, name, health, attack_power, defense, speed, critical_chance):
        super().__init__(name, health, attack_power, defense, speed)
        self.critical_chance = critical_chance

    def precision_shot(self, target):
        if random.random() < self.critical_chance:
            damage = self.attack_power * 2
            print(f"{self.name} lands a Critical Hit on {target.name}! Deals {damage} damage.")
        else:
            damage = self.attack_power
            print(f"{self.name} shoots an arrow at {target.name}. Deals {damage} damage.")

        target.take_damage(damage)


def battle(character1, character2):
    print("\nBATTLE BEGINS! ")
    print(f"{character1.name} vs {character2.name}\n")

    if character1.speed > character2.speed:
        fighters = [character1, character2]
    else:
        fighters = [character2, character1]

    turn = 0
    while character1.is_alive() and character2.is_alive():
        attacker = fighters[turn % 2]
        defender = fighters[(turn + 1) % 2]

        if isinstance(attacker, Warrior) and attacker.health < (attacker.health * 0.3):
            attacker.berserk_mode()
        elif isinstance(attacker, Mage):
            attacker.fireball(defender)
        elif isinstance(attacker, Archer):
            attacker.precision_shot(defender)
        else:
            attacker.attack(defender)

        turn += 1

    winner = character1 if character1.is_alive() else character2
    print(f"\n {winner.name} wins the battle!\n")


warrior = Warrior("Thor", 100, 25, 10, 5)
mage = Mage("Gandalf", 60, 30, 5, 7, 50)
archer = Archer("Alex", 70, 22, 8, 10, 0.3)

battle(warrior, mage)

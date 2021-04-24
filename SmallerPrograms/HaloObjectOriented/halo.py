"""
    [DESCRIPTION]: Python 3 Object Oriented Programming Halo themed.

        This is a sample done just for fun.

        Bullets = ->
        Three burst shot = --->
"""
__title__ = "Halo Object Oriented Programming"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2021, Braiden Gole"
__date__ = "2021-04-24"

class GameCharacter:
    """
    Name        :   GameCharacter
    Purpose     :   This class is where all characters will derive off of.
    """

    def __init__(self, name, health, magazine_count):
        self.name = name
        self.health = health
        self.magazine_count = magazine_count
        self.ammunition_ref = magazine_count

    # Each game character has unique quotes.
    def quote(self, quote):
        return "{0}: {1}".format(self.name, quote)

    def shoot(self):
        self.magazine_count -= 1
        if (self.magazine_count < 1):
            self.reload()

    def reload(self):
        self.magazine_count = self.ammunition_ref

    def __str__(self):
        return self.name + "\n\tHealth: " + str(self.health)

    # When each game character dies.
    def __del__(self):
        return "{0}: has fallen !".format(self.name)

class MasterChief(GameCharacter):
    """
    Name        :   MasterChief
    Purpose     :   This class will hold all methods related to master chief character.
    """
    
    def __init__(self, name, health, magazine_count):
        super(MasterChief, self).__init__(name, health, magazine_count)

    def quote(self, game_quote):
        return super().quote(game_quote)
    
    def shoot(self):
        print("->", end=" ")
        return super().shoot()

    def automatic(self, shoot_amount_of_bullets):
        for bullets in range(0, shoot_amount_of_bullets):
            self.shoot()

    def reload(self):
        print("\n\n{0}: Reloading !\n".format(self.name));
        return super().reload()

class Elite(GameCharacter):
    
    def __init__(self, name, health, magazine_count):
        super(Elite, self).__init__(name, health, magazine_count)

    def quote(self, game_quote):
        return super().quote(game_quote)

    def shoot(self):
        print("--->", end=" ")
        return super().shoot()

    def burst_shot(self, how_many_bursts):
        for bursts in range(0, how_many_bursts):
            for bullets in range(0, 3):
                self.shoot()
    
    def reload(self):
        print("\n\n{0}: Reloading !\n".format(self.name));
        return super().reload()

if __name__ == "__main__":
    
    print()
    master_chief = MasterChief("Master chief", 100, 160)
    print(master_chief.quote("There they are !"))
    print()

    # Master chief sends off 20 bullets.
    master_chief.automatic(20)
    
    print()
    print()

    elite = Elite("Elite", 100, 70)
    print(elite.quote("Wort ! Wort ! Wort !"))

    # 20 shots were fired therefore 20% of life has been taken 1 bullet = 1%.
    elite.health -= 20
    print(elite.name + " Health: " + str(elite.health))
    print()
    elite.burst_shot(2)
    print()

    # The elite fired back a burst shot equal to 2, that suggests that 6 bullets were fired.
    master_chief.health -= 6;
    print()
    print(master_chief.name + " Health: " + str(master_chief.health))
    print()

    master_chief.automatic(140)
    print("Master chief ammunition count: ", master_chief.magazine_count)
    
    elite.health -= 80

    print(elite.__del__())
    master_chief.__del__()


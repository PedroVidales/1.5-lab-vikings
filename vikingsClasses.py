
# Soldier


class Soldier:
    def __init__(self, health, strength):

        self.health=health
        self.strength=strength

    def attack(self):

        return self.strength

    def receiveDamage(self, damage):

        self.health -= damage




# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name=name

    def attack (self):
        return self.strength


        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health>0:
            return '{self.name} has received {damage} points of damage'

        else:
            self.health<0
            return('name has died in act of combat')
        
    def battleCry(self):
        return ('Odin owns you all')



# Saxon


class Saxon(soldier):
    def _init_(self, health, strength):
        Soldier.__init__(self, health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health>0:
            return 'A Saxon has received {damage} points of damage '
        else:
            return 'Saxon has died in combat'






class War:
    pass

class CreatureModel : 
    Attributes = dict (Strength = 3, Agility = 3, Intelligence = 3, Luck = 3)
    def __init__(self, health = 10, dmg = 2) :
        self.health = health + self.Attributes.get("Strength") * 2
        self.dmg = dmg + (self.Attributes.get("Strength") + self.Attributes.get("Agility"))/1.5

from models.CreatureModel import CreatureModel
from EnemyModel import EnemyModel
import random
class PlayerModel(CreatureModel) : 
    def __init__(self):
        pass
    def Attack(self, enemy : EnemyModel) :
        ChanceToHit = random.randint(0,20)
        if ChanceToHit < 7 : 
            return 'unsuccessful'
        if ChanceToHit > 7 :
            return 'successful'
        if ChanceToHit == 20 : 
            return 'Critical'
    def Move(self) : 
        chanceToMeet = random.randint(0,1)
        if chanceToMeet == 1 :
            print("You've met someone")
            return 'zavarushka'
        if chanceToMeet == 0 :
            print("You're still save")
            return 'savezone'
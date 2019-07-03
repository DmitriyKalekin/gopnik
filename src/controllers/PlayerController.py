from MoveCommand import MoveCommand
from AttackCommand import AttackCommand
class PlayerController :
    def __init__(self, attack : AttackCommand, move : MoveCommand) :
        self.attack = attack
        self.move = move
    def Attack(self) : 
        self.attack.execute()
    def Move(self) :
        self.move.execute()


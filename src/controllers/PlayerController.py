from command.MoveCommand import MoveCommand
from command.AttackCommand import AttackCommand
class PlayerController :
    Settings = dict(Move = 'w', Attack = 'a', Exit = 'q')
    def __init__(self, attack : AttackCommand, move : MoveCommand) :
        self.attack = attack
        self.move = move
    def Attack(self) : 
        self.attack.execute()
    def Move(self) :
        self.move.execute()
    def update(self, key) : 
        if key == self.Settings.get('Move') :
            self.Attack()
        if key == self.Settings.get('Attack') :
            self.Move()
        if key == self.Settings.get('Exit') :
            exit()

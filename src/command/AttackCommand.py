from Command import Command
from PlayerModel import PlayerModel
class AttackCommand(Command) : 
    def __init__(self, player : PlayerModel) :
        self.player = PlayerModel
    def execute(self) :
        self.player.Attack()
        pass
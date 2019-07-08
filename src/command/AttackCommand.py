from command.Command import Command
from models.PlayerModel import PlayerModel
class AttackCommand(Command) : 
    def __init__(self, player : PlayerModel) :
        self.player = PlayerModel()
    def execute(self) :
        self.player.Attack()
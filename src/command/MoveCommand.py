from command.Command import Command
from models.PlayerModel import PlayerModel
class MoveCommand(Command) :
    def __init__(self, player) :
        self.player = PlayerModel()
    def execute(self) :
        self.player.Move()
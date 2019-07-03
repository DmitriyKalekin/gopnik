from Command import Command
from PlayerModel import PlayerModel
class MoveCommand(Command) :
    def __init__(self, player) :
        self.player = PlayerModel
    def execute(self) :
        self.player.move()
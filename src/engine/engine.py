from controllers.PlayerController import PlayerController
from models.PlayerModel import PlayerModel
from command.AttackCommand import AttackCommand
from command.MoveCommand import MoveCommand
class Engine : 
    player = PlayerModel()
    playerConsoleInterface = PlayerController(AttackCommand(player), MoveCommand(player))
    @classmethod
    def GameLoop(self) : 
        while True :
            self.playerConsoleInterface.update(input)
import imp
from player import Player
from random import randint
class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.score = 0
    

    def ai_gesture(self):
        self.gesture_list = ["Rock", 'Paper', 'Scissor', 'Lizard', 'Spock']
        self.AI_choice = str(randint(0,4))
        print(f'{self.name} has choosen {self.gesture_list[int(self.AI_choice)]}')
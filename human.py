from player import Player
class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.score = 0
        
    #I need to come back to this and figure out what to do with this code 
    def human_gesture(self):
        self.gesture_list = ["Rock", 'Paper', 'Scissor', 'Lizard', 'Spock']
        choose_gesture = input(f'Please choose your gesture')
        print(f'{self.name} has chosen {choose_gesture}')
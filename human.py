import string
from player import Player
class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.score = 0
        
    #I need to come back to this and figure out what to do with this code 
    def human_gesture(self):
        self.gesture_list = ["Rock", 'Paper', 'Scissor', 'Lizard', 'Spock']
        print('0 is for Rock ')
        print('1 is for Paper')
        print('2 is for Scissors')
        print('3 is for Lizard')
        print('4 is for Spock')
        print('')
        choose_gesture = (input(f'Please choose your gesture. '))
        print(f'{self.name} has chosen {self.gesture_list[int(choose_gesture)]}')
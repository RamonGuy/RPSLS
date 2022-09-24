from human import Human
from ai import AI
player1 = Human('Human')
player2 = AI('AI')
class Game:
    def __init__(self) -> None:
        pass

    def display_welcome(self):
        print("Hello welcome to the RPSLS game!!! ")

    def display_rules(self):
        print('Scissor cuts Paper')
        print('Paper cover Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
        print('Rock crushes Scissors')

    def player_choice(self):
       input("How many players will ne playing? 1, 2, or 3 for a surprise!!!!! ")
       if input == 1:
            player1.human_gesture()
            player2.ai_gesture()
       elif input == 2:
            player1.human_gesture()
            player1.human_gesture
       elif input == 3:
            player2.ai_gesture
            player2.ai_gesture
       else:
            print("Please type in a correct number")
        
            
        
            
        
        


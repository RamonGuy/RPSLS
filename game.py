from human import Human
from ai import AI
player1 = Human('Human')
player2 = AI('AI')
player3 = Human("Human-2")
player4 = AI('AI-2')
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
       user_input = int(input("How many players will be playing? 1, 2, or 3 for a surprise!!!!! "))
       print('')
       if user_input == 1:
            player1.human_gesture()
            player2.ai_gesture()
       elif user_input == 2:
            player1.human_gesture()
            player3.human_gesture()
       elif user_input == 3:
            player2.ai_gesture()
            player4.ai_gesture()
       else:
            print("Please type in a correct number")

    
    def choose_winner(self):
        'Scissors' > 'Paper'
        'Paper' > 'Rock'
        'Rock' > 'Lizard'
        'Lizard' > 'Spock'
        'Spock' > 'Scissors'
        'Scissors' > 'Lizard'
        'Lizard' > 'Paper'
        'Paper' > 'Spock'
        'Spock' > 'Rock'
        'Rock' > 'Scissors'
    
    def round_winner(self):
        if player1.human_choice > player2.AI_choice:
            player1.score += 1
        elif player1.human_choice < player2.AI_choice:
            player2.score += 1
        elif player1.human_choice > player3.human_choice:
            player1.score += 1
        elif player1.human_choice < player3.human_choice:
            player3.score += 1
        elif player2.AI_choice > player4.AI_choice:
            player2.score += 1
        elif player2.AI_choice < player4.AI_choice:
            player4.score += 1

    def display_winner(self):
        if player1.score == 2:
            print('Congratulations you won the RPSLS game!!! ')
        elif player2.score == 2:
            print('Congratulations you won the RPSLS game!!! ')
        elif player3.score == 2:
            print('Congratulations you won the RPSLS game!!! ')
        elif player4.score == 2:
            print('Congratulations you won the RPSLS game!!! ')

    def run(self):
        self.display_welcome()
        print('')
        self.display_rules()
        print('')
        self.player_choice()
        self.choose_winner()
        while self.round_winner() < 2:
            self.round_winner
        self.display_winner()




        
            
        
        


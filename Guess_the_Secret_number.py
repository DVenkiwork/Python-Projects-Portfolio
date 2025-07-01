# Guess the Secret number.py
#

import random

class Game:
    
    def __init__(self,  min_range, max_range, num_players=1):
        self.min_range = min_range
        self.max_range = max_range
        self.num_players = num_players
        self.players = []
        
        # Add new players to the list
        for i in range(self.num_players):
            player_name = input(f"Enter the Player {i+1} name:")
            self.players.append(Player(player_name,random.randint(self.min_range, self.max_range)))
            
        self.game_over = False
        self.current_play_index = 0
        
    def start_game(self):
        print("Welcome to the Guess the Secret Number Game!!")
        print(f"Guess the secret number between {self.min_range} and {self.max_range}")
        
        
    def play_round(self):
        self.start_game()
        
        for player in self.players:
            print(f"\n--- {player.name}'s Turn to guess their number! ---")
            
            while not player.has_won:
                try:
                    guess_number = int(input(f"Player {player.name} guess:"))
                except ValueError:
                    print("Invalid Input, Enter your guess in numbers!")
                    continue
                
                if guess_number > player.secret_number:
                    print(f"Your guess is Higher!")
                    player.attempts_made = player.attempts_made + 1
                elif guess_number < player.secret_number:
                    print("Your guess is Lower!")
                    player.attempts_made = player.attempts_made + 1
                else:
                    print("You got it!!")
                    player.attempts_made = player.attempts_made + 1
                    player.has_won = True
                    break
                
        self.game_over = True
        self.declare_winner()
        
    def declare_winner(self):
        player_attempts = []
        for player in self.players:
            player_attempts.append(player.attempts_made)
        
        min_attempts =  min(player_attempts)
        winners = [x.name for x in self.players if x.attempts_made == min_attempts]   
         # Improve print statement for clarity and to show attempts
        if len(winners) == 1:
            print(f"\n🎉 The WINNER is {winners[0]} with {min_attempts} attempts! 🎉")
        else:
            print(f"\nIt's a TIE! The WINNERS are: {', '.join(winners)} with {min_attempts} attempts each! 🎉")

class Player:
    def __init__(self, name, secret_number):
        self.name = name
        self.attempts_made = 0
        self.has_won = False
        self.secret_number = secret_number
        
if __name__ == "__main__":
    guess_game = Game(10, 50, 1)
    guess_game.play_round()
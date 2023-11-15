"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time


def print_pause(message, wait_time):
    print(message)
    time.sleep(wait_time)


items = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def choose(self):
        return items[0]

    def learn(self, player_move, opp_move):
        pass


class ComputerPlayer(Player):
    def choose(self):
        i = random.randint(0, len(items) - 1)
        return (items[i])

    def learn(self, player_move, opp_move):
        pass


class HumanPlayer(Player):
    def choose(self):
        while True:
            try:
                response = input("""Make your choice : Rock 🪨, Paper 📰 or """
                                 """Scissors ✂️ ? \nDo you want to exit """
                                 """from the game, press [x]\n""").lower()
                if response != 'x' and response in items:
                    break
                else:
                    raise Exception
            except Exception as e:
                print_pause("Please enter a valid choice among items", 0)

        return response

    def learn(self, player_move, opp_move):
        pass


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.opp_move = ""

    def learn(self, player_move, opp_move):
        self.opp_move = opp_move

    def choose(self):
        if self.opp_move == "":
            i = random.randint(0, len(items) - 1)
            return items[i]
        else:
            return self.opp_move


class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.cycle_move = ""

    def choose(self):
        choose = ""
        if self.cycle_move == "":
            choose = Player.move(self)
        else:
            index = items.index(self.cycle_move) + 1
            if index >= len(items):
                index = 0
            choose = items[index]
        self.cycle_move = choose
        return choose

    def learn(self, player_move, opp_move):
        pass


def defeats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class GameSession:

    def __init__(self, ComputerPlayer, HumanPlayer):
        self.ComputerPlayer = ComputerPlayer
        self.HumanPlayer = HumanPlayer
        self.count_wins = 0
        self.count_losses = 0
        self.count_ties = 0

    def play_round(self):
        computer = self.ComputerPlayer.choose()
        human = self.HumanPlayer.choose()
        print_pause(f"Player 1 Move => {computer} \
                    Player 2 Move => {human}", 2)

        if defeats(computer, human):
            self.count_wins += 1
            print_pause(f"wins:{self.count_wins}", 1)
        elif computer == human:
            self.count_ties += 1
            print_pause(f"ties:{self.count_ties}", 1)
        elif defeats(human, computer):
            self.count_losses += 1
            print_pause(f"losses:{self.count_losses}", 1)
        else:
            print_pause("sorry! something went wrong 😕", 2)

        self.score1 = self.count_wins
        self.score2 = self.count_wins
        print_pause(f"Player 1 Score: {self.count_wins} \
                     Player 2 Score: {self.count_losses}\n", 1)

        self.ComputerPlayer.learn(computer, human)
        self.HumanPlayer.learn(human, computer)

    def start_game(self):
        print_pause("Game start! 🎮", 2)
        j = 0
        while j < 10:
            currentRound = j
            print_pause(f"Round {currentRound}:", 1)
            self.play_round()
            j += 1  # update j
        print_pause("\nThanks for playing 🤝", 2)
        print_pause(f"""Final Rounds\nPlayer 1 Points: {self.count_wins}
            Player 2 Points: {self.count_losses}""", 1)
        if self.count_wins > self.count_losses:
            print_pause("Player 1 is Wins!!! 😹\n", 1)
        elif self.count_wins < self.count_losses:
            print_pause("Player 2 is Wins!!! 😹\n", 1)
        else:
            print_pause("It is a DRAW -- Tie Game 😥\n", 1)


if __name__ == '__main__':
    game = GameSession(HumanPlayer(), ComputerPlayer())
    game.start_game()

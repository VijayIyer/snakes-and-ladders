"""
Simulation of a snakes and ladders game
"""
import argparse
import random
import time

def tuple_type(arg:str):
    tuple_arg = arg.split(',')
    return int(tuple_arg[0].strip()), int(tuple_arg[1].strip())


class Game:
    def __init__(self, players, snakes, ladders):
        self.players = [Player(name = player) for player in players]
        self.snakes = [Snake(head = snake[0], tail = snake[1]) for snake in snakes]
        self.ladders = [Ladder(head = ladder[0], tail = ladder[1]) for ladder in ladders]
        self.idx = 0
        self.highest = 100

    def run(self):
        while True:
            cur_player = self.players[self.idx]
            cur_player.move(cur_player.pos + random.randint(1, 6))
            if any(map(lambda x:x.head == cur_player.pos, self.snakes)):
                
                snake = list(filter(lambda x:x.head == cur_player.pos, self.snakes))[0]
                snake.movePlayer(cur_player)
            elif any(list(map(lambda x:x.tail== cur_player.pos, self.ladders))):
                
                ladder = list(filter(lambda x:x.tail == cur_player.pos, self.ladders))[0]
                ladder.movePlayer(cur_player)
            elif cur_player.pos >= self.highest:
                print(f'Game Over:{cur_player.name} has won the game')
                break
            self.idx = (self.idx + 1)%len(self.players)

    def __repr__(self):
        return f'Game Details:\n\
            Players\n:{self.players}\n,\
            Snakes\n:{self.snakes}\n,\
            Ladders\n:{self.ladders}\n'



class Player:
    """
    A player or token which tries to move up the board
    """
    def __init__(self, name):
       self.name = name
       self.pos = 0

    def move(self, to):
        
        print(f'moving {self.name} from {self.pos} to {to}')
        self.pos = to

    def __repr__(self):
       return f'player {self.name} is at square :{self.pos}'


class Snake:
    """
    A snake at a fixed position on the board, which will take a player back to it's tail position
    """
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def movePlayer(self, player):
        print(f'{player.name} stepped on a snake which goes down to {self.tail}')
        player.move(self.tail)
    def __repr__(self):
        return f'snake with it\'s head at {self.head}, and tail at {self.tail}'


class Ladder:
    """
    A ladder at a fixed position on the board, which will take a player up to it's head position
    Parameters
    ------------------------------

    """
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def movePlayer(self, player):
        print(f'{player.name} found a ladder which goes up to {self.head}')
        player.move(self.head)
    def __repr__(self):
        return f'ladder from {self.tail} to {self.head}'


if __name__ == "__main__":
    print('initiating snakes and ladders game')
    # help(Ladder)
    parser = argparse.ArgumentParser()
    parser.add_argument('--players', nargs="+", type=str, required=True)
    parser.add_argument('--snakes', nargs="+", type=tuple_type, required=True)
    parser.add_argument('--ladders', nargs="+", type=tuple_type, required=True)
    args = parser.parse_args()
    print(f'players:{args.players}, snakes:{args.snakes}, ladders:{args.ladders}')
    game = Game(args.players, args.snakes, args.ladders)
    print(game)
    game.run()
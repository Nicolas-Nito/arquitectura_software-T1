import chess.pgn

class MoveParser:
    def __init__(self, pgn_file):
        self.pgn_file = pgn_file
        with open(pgn_file) as pgn:
            self.game = chess.pgn.read_game(pgn)
        self.board = self.game.board()
        self.move_iter = iter(self.game.mainline_moves())
    
    def get_next_move(self):
        try:
            move = next(self.move_iter)
            self.board.push(move)
            return move
        except StopIteration:
            return None
    

if __name__ == "__main__":
    move_parser = MoveParser("game.pgn")
    print(move_parser.get_next_move())
    print(move_parser.get_next_move())
    print(move_parser.get_next_move())
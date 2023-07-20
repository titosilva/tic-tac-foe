from typing import List

def new_game() -> List[str]:
    return [
        '   ',
        '   ',
        '   ',
    ]

def get_winner(game: List[str]) -> str:
    for row in game:
        if row[0] == ' ':
            continue

        if row.count(row[0]) == len(row):
            return row[0]
        
    for col in range(3):
        base = game[0][col]

        if base == ' ':
            continue

        is_winner = True
        for row in game:
            if row[col] != base:
                is_winner = False
                break

        if is_winner:
            return base
        

    if game[1][1] != ' ':
        if game[0][0] == game[1][1] and game[1][1] == game[2][2]:
            return game[1][1]
        
        if game[0][2] == game[1][1] and game[1][1] == game[2][0]:
            return game[1][1]
    
    return ''

def is_full(game: List[str]) -> bool:
    for row in game:
        for col in row:
            if col == ' ':
                return False
            
    return True

def make_move(game: List[str], x: int, y: int, player: str):
    if game[x][y] != ' ':
        raise ValueError()
    
    if x > 2 or y > 2 or x < 0 or y < 0:
        raise ValueError()
    
    game[x] = game[x][:y] + player + game[x][y + 1:]

def draw_game(game: List[str]):
    img = [
        "   |   |   ",
        " {0} | {1} | {2} ".format(game[0][0], game[0][1], game[0][2]),
        "   |   |   ",
        "___________",
        "   |   |   ",
        " {0} | {1} | {2} ".format(game[1][0], game[1][1], game[1][2]),
        "   |   |   ",
        "___________",
        "   |   |   ",
        " {0} | {1} | {2} ".format(game[2][0], game[2][1], game[2][2]),
        "   |   |   ",
    ]
    
    draw_img(img)


def draw_img(img: List[str]):
    for row in img:
        print(row)

if __name__ == "__main__":
    game = new_game()
    draw_game(game)

    current_player = 'O'
    move = (0, 0)
    while True:
        try:
            moves = input(f'Player {current_player}, what is your move? ').strip().split()

            if len(moves) != 2:
                raise ValueError()
            
            move = (int(moves[0]), int(moves[1]))

            make_move(game, move[0], move[1], current_player)
        except KeyboardInterrupt:
            break
        except:
            print('Invalid move!')
            continue

        draw_game(game)

        if get_winner(game) != '':
            print(f'Player {current_player} wins!')
            break

        if is_full(game):
            print(f'Draw!')
            break

        current_player = 'X' if current_player == 'O' else 'O'



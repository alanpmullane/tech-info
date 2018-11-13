game_map = [ [0, 0, 0],
         [0, 0, 0],  
         [0, 0, 0], ]
count = 0

def update_board(game_map, val=0, row=0, col=0):
    try:
        game_map[row][col] = val
    except IndexError as e:
        print("Error: make sure to input row/col < 3", e)
    except Exception as e:
        print("Error: unknown error", e)
    else:
        print("update_board ok")
    finally:
        print("update_board done")
    return game_map

def print_board(game):
    print("   a  b  c")
    for count, row in enumerate(game):
        print(count, row)

game = game_map
print_board(game)

print('...updating')
game = update_board(game, 1, 0, 2)

print_board(game)

#print("   a  b  c")
#for count, row in enumerate(game):
#    print(count, row)



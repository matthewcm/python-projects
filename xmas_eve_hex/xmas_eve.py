from pprint import pprint

NORTH = 'n'
SOUTH = 's'
WEST = 'w'
EAST = 'e'


def flip_tile(pos, flip_dict):
    if str(pos) in flip_dict:
        flip_dict[str(pos)] = not flip_dict[str(pos)]
    else:
        flip_dict[str(pos)] = True


def pos_builder(x, y):
    return f"[{x}, {y}]"


def check_black_tile(x, y, flip_dict):
    if (pos_builder(x, y) in flip_dict):
        return flip_dict[pos_builder(x, y)]
    return False

def neighbor_checker(pos, flip_dict):
    # Only put in new true black to the dict

    new_flip_dict = {}



def neighbor_count(pos, flip_dict):
    count = 0

    x = pos[0]
    y = pos[1]

    # print(check_black_tile(x - 2, y, flip_dict))

    # LEFT
    if check_black_tile(x - 2, y, flip_dict):
        count += 1
    # RIGHT
    if check_black_tile(x + 2, y, flip_dict):
        count += 1
    # NE
    if check_black_tile(x - 1, y + 1, flip_dict):
        count += 1
    # NW
    if check_black_tile(x + 1, y + 1, flip_dict):
        count += 1
    # SW
    if check_black_tile(x - 1, y - 1, flip_dict):
        count += 1
    # SE
    if check_black_tile(x + 1, y - 1, flip_dict):
        count += 1

    return count



    # print (count)


def main():
    with open('input_ex.txt') as f:

        origin = [0, 0]

        flip_dict = {

        }

        lines = f.readlines()

        for steps in lines:

            to_flip_pos = origin.copy()
            i = 0
            while i < len(steps):
                move = steps[i]
                # Does not actually matter if done in two steps, or chunk the moves.
                if move == WEST:
                    to_flip_pos[0] -= 2
                elif move == EAST:
                    to_flip_pos[0] += 2
                elif move == NORTH:
                    to_flip_pos[1] += 1

                    if steps[i + 1] == EAST:
                        to_flip_pos[0] += 1
                    elif steps[i + 1] == WEST:
                        to_flip_pos[0] -= 1

                    i += 1
                elif move == SOUTH:
                    to_flip_pos[1] -= 1

                    if steps[i + 1] == EAST:
                        to_flip_pos[0] += 1
                    elif steps[i + 1] == WEST:
                        to_flip_pos[0] -= 1

                    i += 1

                i += 1

            flip_tile(to_flip_pos, flip_dict)
        #pprint(flip_dict)

        count = 0

        for tile in flip_dict:
            if flip_dict[tile]:
                count += 1

        print(count)

        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0

        for i in range(1, 101):
            for tile in flip_dict:
                if eval(tile)[0] < min_x:
                    min_x = eval(tile)[0]
                elif eval(tile)[0] > max_x:
                    max_x = eval(tile)[0]
                elif eval(tile)[1] > max_y:
                    max_y = eval(tile)[1]
                elif eval(tile)[1] < min_y:
                    min_y = eval(tile)[1]

            new_flip_dict = flip_dict.copy()

            for row in range(min_y - 1, max_y + 1):
                for col in range(min_x - 2, max_x + 2):
                    n_count = neighbor_count(eval(pos_builder(col, row)), flip_dict.copy())

                    #print(f"ncount {n_count}")
                    if pos_builder(col, row) in flip_dict:
                        if (not flip_dict[pos_builder(col, row)]) and n_count == 2:
                            new_flip_dict[pos_builder(col, row)] = True
                        elif flip_dict[pos_builder(col, row)] and (n_count == 0 or n_count > 2):
                            new_flip_dict[pos_builder(col, row)] = False
                    else:
                        if n_count == 2:
                            #print('New flipper')
                            new_flip_dict[pos_builder(col, row)] = True
                        else:
                            new_flip_dict[pos_builder(col, row)] = False

            flip_dict = new_flip_dict.copy()

            #pprint(flip_dict)
            count = 0

            for tile in flip_dict:
                if flip_dict[tile]:
                    count += 1
            print(f"day {i} : {count} ")


if __name__ == '__main__':
    main()

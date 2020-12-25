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


def neighbor_flip(pos, flip_dict, new_flip_dict):
    n_count = neighbor_count(pos, flip_dict)
    if n_count == 2:
        new_flip_dict[pos_builder(pos[0], pos[1])] = True
        return
    if pos_builder(pos[0], pos[1]) in flip_dict:
        if pos_builder(pos[0], pos[1]):
            if n_count == 1:
                new_flip_dict[pos_builder(pos[0], pos[1])] = True
                return


def neighbor_checker(pos, flip_dict):
    # Only put in new true black to the dict

    new_flip_dict = {}

    ne_pos = [pos[0] + 1, pos[1] + 1]
    nw_pos = [pos[0] - 1, pos[1] + 1]
    se_pos = [pos[0] + 1, pos[1] - 1]
    sw_pos = [pos[0] + 1, pos[1] - 1]
    e_pos = [pos[0] + 2, pos[1]]
    w_pos = [pos[0] - 2, pos[1]]

    neighbor_flip(pos, flip_dict, new_flip_dict)

    neighbor_flip(ne_pos, flip_dict, new_flip_dict)
    neighbor_flip(nw_pos, flip_dict, new_flip_dict)
    neighbor_flip(se_pos, flip_dict, new_flip_dict)
    neighbor_flip(sw_pos, flip_dict, new_flip_dict)
    neighbor_flip(e_pos, flip_dict, new_flip_dict)
    neighbor_flip(w_pos, flip_dict, new_flip_dict)

    return new_flip_dict


def neighbor_count(pos, flip_dict):
    count = 0

    x = pos[0]
    y = pos[1]

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


def main():
    with open('input.txt') as f:

        origin = [0, 0]

        flip_dict = {}

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
        # pprint(flip_dict)

        count = 0

        black_tiles = {}

        for tile in flip_dict:
            if flip_dict[tile]:
                black_tiles[tile] = True
                count += 1

        for gen in range(1, 101):

            new_flip_dict = {}
            for tile in black_tiles:

                for black_tile in neighbor_checker(eval(tile), black_tiles.copy()):
                    new_flip_dict[black_tile] = True

            black_tiles = new_flip_dict

            print(f"day {gen} : {len(new_flip_dict)} ")


if __name__ == '__main__':
    main()

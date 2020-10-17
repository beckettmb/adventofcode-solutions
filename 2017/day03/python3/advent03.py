#!/usr/bin/python3


def get_dist(input):
    side_len = 1
    dist_to_cent = 0
    while side_len ** 2 < input:
        side_len += 2
        dist_to_cent += 1

    corner = (side_len - 2) ** 2
    while corner < input:
        corner += (side_len - 1)
    mid = corner - dist_to_cent

    return(abs(input - mid) + dist_to_cent)

def add_row(grid, pos_x, pos_y):
    for row in grid:
        row.insert(0, 0)
        row.append(0)
    grid.insert(0, [])
    grid.append([])

    length = len(grid)
    i = 0
    while i < length:
        grid[0].append(0)
        grid[-1].append(0)
        i += 1

    pos_x += 1
    pos_y += 1
    return grid, pos_x, pos_y

def get_sum(grid, pos_x, pos_y):
    current_val = 0
    for val_y in (pos_y - 1, pos_y, pos_y + 1):
        for val_x in (pos_x - 1, pos_x, pos_x + 1):
            try:
                if val_x >= 0 and val_y >= 0:
                    current_val += grid[val_y][val_x]
            except IndexError:
                pass

    return current_val

def get_val(input):
    current_val = 1
    grid = [[1]]
    pos_x = 0
    pos_y = 0
    direct = 0
    grid, pos_x, pos_y = add_row(grid, pos_x, pos_y)

    while current_val < input:
        if direct == 0:
            if pos_x == len(grid) - 1:
                direct = 1
            else:
                pos_x += 1
        if direct == 1:
            if pos_y == len(grid) - 1:
                direct = 2
            else:
                pos_y += 1
        if direct == 2:
            if pos_x == 0:
                direct = 3
            else:
                pos_x -= 1
        if direct == 3:
            if pos_y == 0:
                direct = 0
                pos_x += 1
            else:
                pos_y -= 1

        if pos_x == len(grid[0]) - 1  and pos_y == 0:
            grid, pos_x, pos_y = add_row(grid, pos_x, pos_y)

        current_val = get_sum(grid, pos_x, pos_y)
        grid[pos_y][pos_x] = current_val

    return current_val


with open('../input.txt', 'r') as f:
    input = int(f.readline())

print(get_dist(input))
print(get_val(input))

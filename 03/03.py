import math

def main():
        # print(first_part(347991))
        print(second_part(347991))

def second_part(inputData):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    data_structure = [[1]]
    size = 1
    direction = LEFT
    res = 1
    x = 0
    y = 0
    while res < inputData:
        x += 1
        if direction == LEFT:
            if len(data_structure[x]) == size:
                size += 1
                res += 1
                direction = UP
                data_structure[x].append(None)
                data_structure.insert([None] * size)
        elif direction == UP
            y += 1
            if len(data_structure) == size:
                size += 1
                res += 1
                direction =
        data_structure[x][y] = res
    print()

def first_part(inputData):
    sqrt_data = math.sqrt(inputData)
    size = math.ceil(sqrt_data)
    full_sq = math.floor(sqrt_data)
    offset = inputData - (full_sq * full_sq)
    steps = 0

    if offset < size:
        steps += max([int(size/2), offset - (size % 2)]) - min([int(size/2), offset - (size % 2)]) + int(size/2) - (1 - (size - full_sq))
    else:
        steps += int(size/2) + max([int(size/2), offset-size]) - min([int(size/2), offset-size])
    return steps


if __name__ == '__main__':
    main()

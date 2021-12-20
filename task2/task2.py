import sys


def include(x, y, x1, y1):
    dist = (x1 ** 2 + y1 ** 2) ** 0.5
    to_circle_dist = (x ** 2 + y ** 2) ** 0.5
    if dist == to_circle_dist - r or dist == to_circle_dist + r:
        return 0
    elif to_circle_dist + r > dist > to_circle_dist - r:
        return 1
    elif dist > to_circle_dist + r or dist < to_circle_dist - r:
        return 2


if __name__ == '__main__':
    x = 0
    y = 0
    r = 0
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]
    with open(file_name1, 'r') as f1:
        for line in f1:
            line.endswith('\n')
            if len(line.split()) == 2:
                line = line.split()
                x = int(line[0])
                y = int(line[1])
            elif len(line.split()) == 1:
                r = int(line)

    x1 = 0
    y1 = 0
    with open(file_name2, 'r') as f2:
        for line in f2:
            line.endswith('\n')
            line = line.split()
            x1 = int(line[0])
            y1 = int(line[1])
            print(include(x, y, x1, y1))



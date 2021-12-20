import sys


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    num = ''
    start = 1
    while True:
        for i in range(start, start + m):
            if i > n:
                i %= n
                num += str(i)
            else:
                num += str(i)
        start = int(num[-1])
        if num[-1] == '1':
            break
    answer = ''
    for i in range(0, len(num), m):
        answer += num[i]
    print(answer)

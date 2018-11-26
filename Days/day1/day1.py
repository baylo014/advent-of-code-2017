import time
def part1():
    with open("day1.txt") as inputFile:
        txt = inputFile.read()[:-1]
        l = len(txt)
        sum = 0
        s = time.time()
        for i in range(l):
            f = int(txt[i])
            n = int(txt[(i+1) % l])
            if f == n:
                sum += f
        e = time.time()
    print("TIME 1",e-s)
    print("SUM 1",sum)
def part2():
    with open("day1.txt") as inputFile:
        txt = inputFile.read()[:-1]
        l = len(txt)
        mid = l // 2
        sum = 0
        s = time.time()
        for i in range(l):
            f = int(txt[i])
            n = int(txt[(i+mid)%l])
            if f == n:
                sum += f
        e = time.time()
    print("TIME 2",e-s)
    print("SUM 2",sum)
def main():
    part1()
    part2()
if __name__ == '__main__':
    main()

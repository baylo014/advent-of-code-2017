def dup(values,sort=False):
    output = []
    seen = set()
    for value in values:
        if sort:
            value = ''.join(sorted(value))
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
def Part1():
    count = 0
    with open("day4.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            line2 = " ".join(dup(words))
            if len(line.strip()) == len(line2.strip()):
                count+=1
    print(count)
def Part2():
    count = 0
    with open("day4.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            line2 = " ".join(dup(words,True))
            if len(line.strip()) == len(line2.strip()):
                count+=1
    print(count)
    print()
def main():
    Part1()
    Part2()
if __name__ == '__main__':
    main()

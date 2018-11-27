def partA():
    sum = 0
    with open("day2.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            line = list(map(lambda x: int(x), line))
            maxLine = max(line)
            minLine = min(line)
            sum += (maxLine-minLine)
    print(sum)
def partB():
    sum = 0
    with open("day2.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            line = list(map(lambda x: int(x), line))
            for i in range(0,(len(line)-1)):
                for j in range((i+1),(len(line))):
                    if (line[i] % line[j]) == 0 :
                        sum += (line[i]//line[j])
                    elif (line[j] % line[i]) == 0:
                        sum += (line[j]//line[i])
    print(sum)
def main():
    partA()
    partB()
if __name__ == '__main__':
    main()

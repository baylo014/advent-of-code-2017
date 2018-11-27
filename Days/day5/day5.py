def part1():
    maze=[]
    with open("day5.txt") as f:
        temp = f.readlines()
        maze = list(map(lambda x:int(x),temp))
    loc = 0
    steps = 0
    newPos = 0
    while(len(maze) > loc > -1):
        newPos = loc + maze[loc]
        maze[loc] += 1
        loc = newPos
        steps += 1
    print(steps)
def part2():
    maze=[]
    with open("day5.txt") as f:
        temp = f.readlines()
        maze = list(map(lambda x:int(x),temp))
    loc = 0
    steps = 0
    newPos = 0
    while(len(maze) > loc > -1):
        newPos = loc + maze[loc]
        if maze[loc] >= 3:
            maze[loc] -= 1
        else:
            maze[loc] += 1
        loc = newPos
        steps += 1
    print(steps)
def main():
    part1()
    part2()
if __name__ == '__main__':
    main()

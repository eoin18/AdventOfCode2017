#!/usr/bin/env python

def main():
    steps = 0
    position = 0
    instructions = []
    with open('data.txt') as f:
        lines = f.readlines()
        for line in lines:
            instructions.append(int(line.strip('\n')))
    while position >= 0 and position < len(instructions):
        temp = position
        position += instructions[position]
        if instructions[temp] >= 3:
            instructions[temp] -= 1
        else:
            instructions[temp] += 1
        steps += 1
    print steps

if __name__ == "__main__":
    main()
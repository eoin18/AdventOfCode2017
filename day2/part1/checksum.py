#!/usr/bin/env python


def checksum_line(line):
    min = 0
    max = 0
    for split in line.split('\t'):
        number = int(split)
        if number > max or max == 0:
            max = number
        if number < min or min == 0:
            min = number
    return max - min

def main():
    checksum = 0
    with open('data.txt') as f:
        for line in f.readlines():
            checksum += checksum_line(line)
    print checksum

if __name__ == "__main__":
    main()
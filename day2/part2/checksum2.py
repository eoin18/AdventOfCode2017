#!/usr/bin/env python


def checksum_line(line):
    line_split = line.split('\t')
    for i in range(0, len(line_split)):
        number = int(line_split[i])
        for j in range(0, len(line_split)):
            divisor = int(line_split[j])
            if i != j and number % divisor == 0:
                return number / divisor

def main():
    checksum = 0
    with open('data.txt') as f:
        for line in f.readlines():
            checksum += checksum_line(line)
    print checksum

if __name__ == "__main__":
    main()
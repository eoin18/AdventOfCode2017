#!/usr/bin/env python


def main():
    sum = 0
    with open("data.txt") as input_file:
        input = input_file.read()
        for i in range(0, len(input)):
            target = (i + (len(input) / 2)) % len(input)
            if input[i] == input[target]:
                sum += int(input[i])
    print sum

if __name__ == "__main__":
    main()

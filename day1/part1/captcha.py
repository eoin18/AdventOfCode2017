#!/usr/bin/env python


def main():
    sum = 0
    with open("data.txt") as input_file:
        input = input_file.read()
        for i in range(0, len(input)-1):
            if input[i] == input[i+1]:
                sum += int(input[i])
        if input[len(input)-1] == input[0]:
            sum += int(input[len(input)-1])
    print sum

if __name__ == "__main__":
    main()

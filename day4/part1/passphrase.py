#!/usr/bin/env python


def is_valid_passphrase(line):
    tokens = {}
    line_split = line.split(' ')
    for token in line_split:
        word = token.strip('\n')
        if word in tokens:
            return False
        else:
            tokens[word] = 1
    return True

def main():
    valids = 0
    with open('data.txt') as f:
        for line in f.readlines():
            if is_valid_passphrase(line):
                valids += 1
    print valids

if __name__ == "__main__":
    main()
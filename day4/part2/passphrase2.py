#!/usr/bin/env python


def is_anagram(word, tokens):
    for token in tokens:
        if sorted(token) == sorted(word):
            return True
    return False

def is_valid_passphrase(line):
    tokens = []
    line_split = line.split(' ')
    for token in line_split:
        word = token.strip('\n')
        if is_anagram(word, tokens):
            return False
        else:
            tokens.append(word)
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
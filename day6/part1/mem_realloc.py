#!/usr/bin/env python


def reallocate(state):
    new_state = list(state)
    largest_index = 0
    max = 0
    for i in range(0, len(state)):
        if state[i] > max:
            largest_index = i
            max = state[i]
    new_state[largest_index] = 0
    curr_index = largest_index + 1
    if curr_index >= len(state): curr_index = 0
    print max
    while max > 0:
        for i in range(curr_index, len(state)):
            new_state[i] += 1
            max -= 1
            if max == 0:
                return new_state
        curr_index = 0
    return new_state

def main():
    steps = 0
    state = []
    prev_states = {}
    with open('data.txt') as f:
        lines = f.readlines()
        for line in lines:
            for token in line.split('\t'):
                state.append(int(token.strip('\n')))
    print state
    while ','.join(str(x) for x in state) not in prev_states:
        string_rep = ','.join(str(x) for x in state)
        prev_states[string_rep] = 1
        state = reallocate(state)
        print state
        steps += 1
    print steps

if __name__ == "__main__":
    main()
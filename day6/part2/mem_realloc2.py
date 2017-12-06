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
    while max > 0:
        for i in range(curr_index, len(state)):
            new_state[i] += 1
            max -= 1
            if max == 0:
                return new_state
        curr_index = 0
    return new_state

def main():
    state = []
    with open('data.txt') as f:
        lines = f.readlines()
        for line in lines:
            for token in line.split('\t'):
                state.append(int(token.strip('\n')))
    state = find_loop(state)
    find_loop(state)


def find_loop(initial_state):
    steps = 0
    prev_states = {}
    while ','.join(str(x) for x in initial_state) not in prev_states:
        string_rep = ','.join(str(x) for x in initial_state)
        prev_states[string_rep] = 1
        initial_state = reallocate(initial_state)
        steps += 1
    print steps
    return initial_state


if __name__ == "__main__":
    main()
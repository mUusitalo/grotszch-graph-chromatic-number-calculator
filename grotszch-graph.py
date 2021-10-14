import itertools
import numpy as np

PRINT_FREQUENCY = 1000

NODES = (
    (3, 4, 5, 6, 2),
    (1, 8, 11),
    (1, 7, 9),
    (1, 8, 10),
    (1, 9, 11),
    (1, 7, 10),
    (3, 6, 8, 11),
    (2, 4, 7, 9),
    (3, 5, 8, 10),
    (4, 6, 9, 11),
    (2, 5, 7, 10),
)

def has_no_collisions(combination, index):
    index_color = combination[index]
    for node_number in NODES[index]:
        if combination[node_number - 1] == index_color:
            return False
    return True

def is_valid_combination(combination):
    return all(has_no_collisions(combination, i) for i in range(len(combination)))

def all_combinations_with_repeats(seq, length):
    for i in range(len(seq) ** length):
        yield tuple(map(int, np.base_repr(i, len(seq)).zfill(length)))

def main():
    colors = tuple(range(int(input("Enter number of colors: ")))) 
    total = 0
    valid = 0
    number_of_possible_combinations = len(colors) ** len(NODES)
    valid_combinations = []
    for comb_with_repeats in all_combinations_with_repeats(colors, len(NODES)):
        if is_valid_combination(comb_with_repeats):
            valid_combinations.append(comb_with_repeats)
            valid += 1
            if valid % PRINT_FREQUENCY == 0:
                print(f"{total}/{number_of_possible_combinations}", flush=True)
        total += 1
    
    print("Valid combinations:\n")
    for combination in valid_combinations:
        print(combination)
    print(f"\n{len(valid_combinations)} valid color combinations out of {total} ({len(colors)}^{len(NODES)}) total combinations")

if __name__ == '__main__':
    main()
import itertools


def is_potential_match(correct_positions, correct_symbols, guess, potential_match):
    guess = list(guess)
    potential_match = list(potential_match)
    index = 0
    c_pos = 0
    while index < len(potential_match):
        if guess[index] == potential_match[index]:
            del guess[index]
            del potential_match[index]
            c_pos = c_pos + 1
        else:
            index = index + 1
    if c_pos != correct_positions:
        return False

    c_symbols = 0
    for c in guess:
        if c in potential_match:
            c_symbols = c_symbols + 1
            potential_match.remove(c)

    return c_symbols == correct_symbols


def remove_non_potential_matches(correct_positions, correct_symbols, guess, combinations):
    index = 0
    while index < len(combinations):
        if is_potential_match(correct_positions, correct_symbols, guess, combinations[index]):
            index = index + 1
        else:
            del combinations[index]


def generate_symbols(number):
    return list(map(chr, range(97, 97 + number)))


def game(number_of_symbols, number_of_slots):
    valid_symbols = generate_symbols(number_of_symbols)
    print("Valid Symbols : ", valid_symbols)
    combinations = [p for p in itertools.product(valid_symbols, repeat=number_of_slots)]

    found = None
    total_combinations = len(combinations)
    print("Total combinations : ", total_combinations)
    while found != "yes":

        guess = input("What was the guess?")
        correct_pos = int(input("How many positions are correct ?"))
        correct_symbol = int(input("How many symbols are correct, but on wrong position ?"))
        remove_non_potential_matches(correct_pos, correct_symbol, guess, combinations)
        total_combinations = len(combinations)
        print("Total combinations : ", total_combinations)
        found = input("Did you find ?")
        print("Try this one : ", combinations[0])


if __name__ == '__main__':
    game(3, 3)




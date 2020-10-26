import itertools


def get_symbols_on_correct_position(guess, potential_match):
    corrects = list()
    for g_c, p_c in zip(guess, potential_match):
        if g_c == p_c:
            corrects.append(g_c)
    return corrects


def get_total_correct_symbols(guess, potential_match):
    for c in guess:
        if c in potential_match:
            potential_match.remove(c)
    return len(guess) - len(potential_match)


def is_potential_match(correct_positions, correct_symbols, guess, potential_match):
    corrects = get_symbols_on_correct_position(guess, potential_match)
    if len(corrects) != correct_positions:
        return False

    guess = list(guess)
    potential_match = list(potential_match)
    for c in corrects:
        guess.remove(c)
        potential_match.remove(c)

    return get_total_correct_symbols(guess, potential_match) == correct_symbols


def get_potential_matches(correct_positions, correct_symbols, guess, codes):
    return tuple(filter(lambda code: is_potential_match(correct_positions, correct_symbols, guess, code), codes))


def generate_symbols(number):
    return tuple(map(chr, range(97, 97 + number)))


def game(number_of_symbols, number_of_slots):
    valid_symbols = generate_symbols(number_of_symbols)
    print("Valid Symbols : ", valid_symbols)
    combinations = [p for p in itertools.product(valid_symbols, repeat=number_of_slots)]

    found = None
    total_combinations = len(combinations)
    print("Total combinations : ", total_combinations)
    while found != "yes":
        print("Try this one : ", combinations[0])
        guess = input("What was the guess?")
        correct_pos = int(input("How many positions are correct ?"))
        correct_symbol = int(input("How many symbols are correct, but on wrong position ?"))
        combinations = get_potential_matches(correct_pos, correct_symbol, guess, combinations)
        total_combinations = len(combinations)
        print("Total combinations : ", total_combinations)
        found = input("Did you find ?")


if __name__ == '__main__':
    game(8, 6)




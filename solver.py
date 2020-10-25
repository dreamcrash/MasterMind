import itertools


def is_potential_match(correct_positions, correct_symbols, code, secret_code):
    code_l = list(code)
    secret_code_l = list(secret_code)
    index = 0
    c_pos = 0
    while index < len(secret_code_l):
        if code_l[index] == secret_code_l[index]:
            del code_l[index]
            del secret_code_l[index]
            c_pos = c_pos + 1
        else:
            index = index + 1
    if c_pos != correct_positions:
        return False

    c_symbols = 0
    for c in code_l:
        if c in secret_code_l:
            c_symbols = c_symbols + 1
            secret_code_l.remove(c)

    return c_symbols == correct_symbols


def filter_potential_matches(correct_positions, correct_symbols, code, list_of_combinations):
    index = 0
    while index < len(list_of_combinations):
        if is_potential_match(correct_positions, correct_symbols, code, list_of_combinations[index]):
            index = index + 1
        else:
            del list_of_combinations[index]


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
        filter_potential_matches(correct_pos, correct_symbol, guess, combinations)
        total_combinations = len(combinations)
        print("Total combinations : ", total_combinations)
        found = input("Did you find ?")
        print("Try this one : ", combinations[0])


if __name__ == '__main__':
    game(6, 4)




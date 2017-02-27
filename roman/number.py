__author__ = 'Cassio dos Santos Sousa'

roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def to_number(roman):
    final_number = 0
    current_sum = 0
    prev = None

    for letter in roman:
        if prev is None:
            prev = letter

        if prev == letter:
            current_sum += roman_map[letter]

        else:
            if roman_map[prev] == 5 * roman_map[letter]:  # Cover the cases with 6, 7 and 8
                current_sum += roman_map[letter]
                prev = letter

            else:
                if roman_map[letter] > roman_map[prev]:  # Cover the cases with 4 and 9
                    current_sum = roman_map[letter] - current_sum
                    final_number += current_sum
                    current_sum = 0
                    prev = None

                else:  # Goes to the next set of ten
                    final_number += current_sum
                    current_sum = roman_map[letter]
                    prev = letter

    if current_sum > 0:
        final_number += current_sum

    return final_number

__author__ = 'Cassio dos Santos Sousa'


def to_roman(num):
    if num <= 0 or num >= 4000:
        return ValueError('Number cannot be converted to Roman')

    ones = ['I', 'X', 'C', 'M']
    fives = ['V', 'L', 'D']

    full_number = ''
    current_pointer = 0

    while num > 0:
        modulo_ten = num % 10
        current_section = ''

        if modulo_ten == 9:
            current_section += ones[current_pointer] + ones[current_pointer + 1]

        elif modulo_ten == 4:
            current_section += ones[current_pointer] + fives[current_pointer]

        else:
            if modulo_ten >= 5:
                current_section += fives[current_pointer]
                modulo_ten -= 5

            while modulo_ten > 0:
                current_section += ones[current_pointer]
                modulo_ten -= 1

        full_number = current_section + full_number
        current_pointer += 1
        num /= 10

    return full_number

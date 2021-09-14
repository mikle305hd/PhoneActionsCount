import re
from typing import Tuple

buttons = {
    1: ['1'], 2: ['2', 'a', 'b', 'c'], 3: ['3', 'd', 'e', 'f'],
    4: ['4', 'g', 'h', 'i'], 5: ['5', 'j', 'k', 'l'], 6: ['6', 'm', 'n', 'o'],
    7: ['7', 'p', 'q', 'r', 's'], 8: ['8', 't', 'u', 'v'], 9: ['9', 'w', 'x', 'y', 'z'],
    10: ['*'], 11: ['0'], 12: ['#']
}


def add_asterisks(word: str) -> str:
    """
    Adding asterisk before first upper case and before every case change
    :param word: word with digits and letters only
    :return: word with asterisks before each case change
    """
    new_word = ''
    # Доходим до первой большой буквы
    for i, char in enumerate(word):
        if char.islower() or char.isdigit():
            new_word += char
        else:
            word = word[i:]
            new_word += '*'
            break
    previous_letter = -1
    for char in word:
        if (previous_letter != -1) and (previous_letter.isupper() != char.isupper()):
            new_word += f'*{char}'
        else:
            new_word += char
        if not char.isdigit():
            previous_letter = char
    return new_word


def get_indexes_from_num(number: int) -> Tuple[int, int]:
    """
    Getting indexes (row and column) of matrix with a dictionary key
    :param number: dictionary key - button on phone keyboard 4x3
    :return: indexes - row and column
    """
    # Находим индексы нужного номера (ключа)
    if number in range(1, 4):
        row = 0
    elif number in range(4, 7):
        row = 1
    elif number in range(7, 10):
        row = 2
    else:
        row = 3
    number %= 3
    column = (number - 1) if (number in range(1, 3)) else 2
    return (row, column)


def go_to_target(selected_key: int, target_key: int) -> int:
    """
    Counts moves that need to go from selected key to target key
    :param selected_key: start dictionary key
    :param target_key: end dictionary key
    :return: count of clicks which need to reach end number key
    """
    moves = 0
    (start_row, start_column) = get_indexes_from_num(selected_key)
    (end_row, end_column) = get_indexes_from_num(target_key)
    # Finding optimal variant: row
    rows_dif = end_row - start_row
    if abs(rows_dif) <= 2:
        moves += abs(rows_dif)
    else:
        moves += 1
    # Finding optimal variant: column
    col_dif = end_column - start_column
    if abs(col_dif) <= 1:
        moves += abs(col_dif)
    else:
        moves += 1

    return moves


def get_key_from_char(char: str) -> Tuple[int, int]:
    """
    Getting key from symbol
    :param char:
    :return: key on phone keyboard 4x3, count of clicks on key needed after key select
    """
    # Достаем ключ (номер) символа (цифры, буквы, звёздочки, решётки) на который нужно нажать
    for key, chars in buttons.items():
        # buttons[key] - массив символов принадлежащих определенному номеру (ключу)
        for counter in range(0, len(chars)):
            if char == chars[counter]:
                return (key, counter)


def main():
    print('Введите слово:', end=' ')
    word = input()
    # Проверка на валидность
    if not (re.compile('[@_!#$%^&*()<>?/\|}{~: ]').search(word) == None):
        print('Ошибка валидности: введёная строка содержит специальные символы или пробелы')
        return
    word = add_asterisks(word).lower()

    all_clicks = 0
    previous_char = '1'
    for char in word:
        # clicks - количество нажатий требуемое для нынешнего символа
        (prev_key, clicks) = get_key_from_char(previous_char)
        (key, clicks) = get_key_from_char(char)
        clicks += go_to_target(prev_key, key)
        # 2 раза ОК для подтверждения
        if key in range(2, 10):
            clicks += 2
        # 1 раз ОК для 1, *, 0, #
        else:
            clicks += 1

        all_clicks += clicks
        previous_char = char

    print(f'Требуемое количество нажатий на пульте дистанционного управления равно {all_clicks}')


if __name__ == '__main__':
    main()
buttons = {
    1: ['1'], 2: ['2', 'a', 'b', 'c'], 3: ['3', 'd', 'e', 'f'],
    4: ['4', 'g', 'h', 'i'], 5: ['5', 'j', 'k', 'l'], 6: ['6', 'm', 'n', 'o'],
    7: ['7', 'p', 'q', 'r', 's'], 8: ['8', 't', 'u', 'v'], 9: ['9', 'w', 'x', 'y', 'z'],
    10: ['*'], 11: ['0'], 12: ['#']
}


def add_asterisks(word: str) -> str:
    """
    :param word: string (word) with digits and letters
    :return: string (word) with asterisks before each case change
    """
    new_word = ''
    # Доходим до первой большой буквы
    for i in range(0, len(word)):
        if word[i].islower() or word[i].isdigit():
            new_word += word[i]
        else:
            word = word[i:]
            new_word += '*'
            break
    previous_letter = -1
    for i in range(0, len(word)):
        if (previous_letter != -1) and (previous_letter.isupper() != word[i].isupper()):
            new_word += f'*{word[i]}'
        else:
            new_word += word[i]
        if not word[i].isdigit():
            previous_letter = word[i]
    return new_word

def get_indexes_from_num(number: int):
    """
    :param number: number (key) - button on phone keyboard 4x3
    :return: tuple(row, column) - indexes
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
    :param selected_key:
    :param target_key:
    :return: int count of clicks that needs to reach end number key
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

def get_num_from_symbol(symbol: str) -> (int, int):
    """
    :param symbol:
    :return: tuple(number, clicks) - button on phone keyboard 4x3, clicks on key after key select
    """
    # Достаем ключ (номер) символа (цифры, буквы, звёздочки, решётки) на который нужно нажать
    for key in buttons:
        # buttons[key] - массив символов принадлежащих определенному номеру (ключу)
        for i in range(0, len(buttons[key])):
            if symbol == buttons[key][i]:
                return (key, i)

def main():
    print('Введите слово:', end=' ')
    word = add_asterisks(input()).lower()
    all_clicks = 0

    previous_char = '1'
    for char in word:
        # clicks - количество нажатий на все кнопки
        (prev_key, clicks) = get_num_from_symbol(previous_char)
        (key, clicks) = get_num_from_symbol(char)
        clicks += go_to_target(prev_key, key)
        # 2 раза ОК для подтверждения
        if key in range(2, 10):
            clicks += 2
        # 1 раз ОК для 1, *, 0, #
        else:
            clicks += 1

        all_clicks += clicks
        previous_char = char

    print(f'Требуемое количество нажатий на пульте дистанционного управления равно {all_clicks}', end='')

if __name__ == '__main__':
    main()

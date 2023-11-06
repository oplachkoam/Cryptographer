russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
english_alphabet = "abcdefghijklmnopqrstuvwxyz"

visener_table_russian = [[0] * 33 for _ in range(33)]
visener_table_english = [[0] * 26 for _ in range(26)]

letters_cesar_russian = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д', 'п', 'у', 'я', 'ы', 'ь', 'г',
                         'з', 'б', 'ч', 'й', 'х', 'ж', 'ш', 'ю', 'ц', 'щ', 'э', 'ф', 'ъ', 'ё']
percents_cesar_russian = [11.0, 8.45, 8.01, 7.35, 6.70, 6.26, 5.47, 4.73, 4.54, 4.40, 3.49, 3.21, 2.98, 2.81, 2.62,
                          2.01, 1.90, 1.74, 1.70, 1.65, 1.59, 1.44, 1.21, 0.97, 0.94, 0.73, 0.64, 0.48, 0.36, 0.32,
                          0.26, 0.04, 0.04]

letters_cesar_english = ['e', 't', 'o', 'a', 'n', 'i', 'r', 's', 'h', 'd', 'l', 'c', 'f', 'u', 'm', 'p', 'y', 'w', 'g',
                         'b', 'v', 'k', 'x', 'j', 'q', 'z']
percents_cesar_english = [10.5, 7.2, 6.5, 6.3, 5.9, 5.5, 5.4, 5.2, 4.7, 3.5, 2.9, 2.3, 2.25, 2.25, 2.1, 1.75, 1.2, 1.2,
                          1.1, 1.05, 0.8, 0.3, 0.2, 0.1, 0.1, 0.1]

for i in range(33):
    for j in range(33):
        visener_table_russian[i][j] = russian_alphabet[(i + j) % 33]

for i in range(26):
    for j in range(26):
        visener_table_english[i][j] = english_alphabet[(i + j) % 26]


def most_popular_item(array):
    """
    finds most common item in list

    :param array: list
    :return: most common item
    """

    maxi = 0
    item = None
    array = sorted(array)
    for i in set(array):
        a = array.count(i)
        if a > maxi:
            maxi = a
            item = i
    return item


def language_definition(line):
    """
    defines on what language line is written

    :param line: the string in which the language will be defined
    :return: language of the string: english or russian; or
    None, if both languages in line or no letters in it
    """

    rus_flag = False
    en_flag = False
    for i in line:
        if i in russian_alphabet:
            rus_flag = True
        if i in english_alphabet:
            en_flag = True
    if rus_flag and en_flag:
        return None
    elif rus_flag:
        return russian_alphabet
    elif en_flag:
        return english_alphabet
    else:
        return None


def line_formatting(line):
    """
    makes all letters small; deletes
    dots, commas and other symbols
    to make hack harder

    :param line: string that will be formatted
    :return: changed line
    """
    line = line.replace('-', ' ')
    res = ''
    for i in line:
        if i.isalpha():
            res += i.lower()
        elif i != ' ' and i != '\n':
            pass
        else:
            res += i
    return res


def cesar_encrypting(line, a):
    """
    encrypting a line using the cesar method

    :param line: line that will be encrypted
    :param a: offset of each letter
    :return: encrypted line
    """

    line = line_formatting(line)
    res = ''
    language = language_definition(line)
    for i in line:
        if i.isalpha():
            res += language[(language.find(i) + a) % len(language)]
        else:
            res += i

    return res


def dynamic_cesar_encrypting(line, a):
    """
    encrypting a line using the dynamic cesar method

    :param line: line that will be encrypted
    :param a: offset of first letter
    :return: encrypted line
    """

    line = line_formatting(line)
    res = ''
    language = language_definition(line)
    for i in line:
        if i.isalpha():
            res += language[(language.find(i) + a + len(res)) % len(language)]
        else:
            res += i

    return res


def visener_encrypting(line, key):
    """
    encrypting a line using the visener method

    :param line: line that will be encrypted
    :param key: key that using for encrypting
    :return: encrypted line
    """

    line = line_formatting(line)
    key = line_formatting(key).lower().replace(' ', '')
    language = language_definition(line)
    if language == russian_alphabet:
        table = visener_table_russian
    else:
        table = visener_table_english
    while len(key) < len(line):
        key += key

    res = ''
    for i in range(len(line)):
        if line[i].isalpha():
            res += table[language.find(key[i])][language.find(line[i])]
        else:
            res += line[i]

    return res


def verman_encrypting(line, key):
    """
    encrypting a line using the verman method

    :param line: line that will be encrypted
    :param key: key that using for encrypting
    :return: encrypted line
    """

    count = 0
    line = line_formatting(line)
    key = line_formatting(key).lower().replace(' ', '')
    language = language_definition(line)
    while len(key) < len(line):
        key += key
    res = ''
    for i in range(len(line)):
        if line[i].isalpha():
            res += language[(language.find(line[i]) + language.find(key[count])) % len(language)]
            count += 0
        else:
            res += line[i]

    return res


def cesar_decrypt(line, a):
    """
    decrypt a line encrypted by the cesar method

    :param line: line that will be decrypt
    :param a: offset of each letter
    :return: decrypted line
    """

    line = line_formatting(line)
    res = ''
    language = language_definition(line)
    for i in line:
        if i.isalpha():
            res += language[(language.find(i) - a) % len(language)]
        else:
            res += i

    return res


def dynamic_cesar_decrypt(line, a):
    """
    decrypt a line encrypted by the dynamic cesar method

    :param line: line that will be decrypt
    :param a: offset of first letter
    :return: decrypted line
    """

    line = line_formatting(line)
    res = ''
    offset = 0
    language = language_definition(line)
    for i in line:
        if i.isalpha():
            res += language[(language.find(i) - a - offset) % len(language)]
        else:
            res += i
        offset += 1

    return res


def verman_decrypt(line, key):
    """
    decrypting a line encrypted by verman method

    :param line: line that will be decrypted
    :param key: key that was used for encrypting
    :return: decrypted line
    """

    count = 0
    line = line_formatting(line)
    key = line_formatting(key).lower().replace(' ', '')
    language = language_definition(line)
    if language == russian_alphabet:
        table = visener_table_russian
    else:
        table = visener_table_english
    while len(key) < len(line):
        key += key
    res = ''

    for i in range(len(line)):
        if line[i].isalpha():
            res += language[table[language.find(key[count])].index(line[i])]
            count += 1
        else:
            res += line[i]

    return res


def visener_decrypt(line, key):
    """
    decrypting a line encrypted by visener method

    :param line: line that will be decrypted
    :param key: key that was used for encrypting
    :return: decrypted line
    """

    line = line_formatting(line)
    key = line_formatting(key).lower().replace(' ', '')
    language = language_definition(line)
    while len(key) < len(line):
        key += key

    res = ''
    for i in range(len(line)):
        if line[i].isalpha():
            res += language[(language.find(line[i]) - language.find(key[i])) % len(language)]
        else:
            res += line[i]

    return res


def auto_hack_cesar(line, key=None):
    """
    hack cesar encryption without offset

    :param line: encrypted line
    :return: decrypted line
    """

    frequency = []
    possible_offsets = []
    line = line_formatting(line)
    len_no_spaces = len(line.replace(' ', ''))
    if language_definition(line) == english_alphabet:
        language = english_alphabet
        often_letters = letters_cesar_english
        often_percents = percents_cesar_english
        if len(line) < 100:
            accuracy = 500 // len(line)
        else:
            accuracy = 5
    else:
        language = russian_alphabet
        often_letters = letters_cesar_russian
        often_percents = percents_cesar_russian
        accuracy = 50
    for i in language:
        frequency.append(line.count(i) / len_no_spaces * 100)
    for x in range(len(often_letters)):
        for y in range(len(language)):
            if abs(often_percents[x] - frequency[y]) * 100 / often_percents[x] < accuracy:
                if y > language.find(often_letters[x]):
                    possible_offsets.append(y - language.find(often_letters[x]))
                else:
                    possible_offsets.append(len(language) + y - language.find(often_letters[x]))
    offset = most_popular_item(possible_offsets)
    return cesar_decrypt(line, offset)

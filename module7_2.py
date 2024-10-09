from pprint import pprint

def custom_write(file_name, strings):
    string_positions = {}
    line_number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte = file.tell()
        file.write(string + '\n')
        string_positions[(line_number, byte)] = string
        line_number += 1
    file.close()
    return string_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
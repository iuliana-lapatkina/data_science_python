class Numbers(Exception):
    def __init__(self, txt):
        self.txt = txt

result_list = []

while True:
    value = input('Введите число или stop для выхода: ')

    if value == 'stop':
        print(f'Список чисел: {result_list}')
        break

    try:
        if not value.isnumeric():
            raise Numbers('NaN!')
        result_list.append(int(value))
    except Numbers as error:
        print('Введите число')

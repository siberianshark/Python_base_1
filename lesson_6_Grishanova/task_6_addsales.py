import sys
import os

STRING_LENGTH = 7

if len(sys.argv) < 2:
    print('Введите значение')
    sys.exit(1)
else:
    with open(os.path.join('data', 'bakery.csv'), 'a', encoding='utf-8') as f:
        script, amount =sys.argv
        try:
            amount_iny = float(amount.replace(',', '.'))
            f.write(f'{amount.zfill(STRING_LENGTH - 1)}\n')
        except ValueError:
            print('Введите значение в формате "число,число"')
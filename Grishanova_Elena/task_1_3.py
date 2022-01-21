def transform_string(element) -> str:
    numbers = [20, 21, 22, 23]
    if element in numbers:
        return f'{element} процентов'
    if element % 10 == 1:
        return f'{element} процент'
    if 1 < element % 10 <5:
        return f'{element} процента'
    else:
        return f'{element} процентов'


n = 101
for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
#a
def transfer_list_in_str(list_in:list) -> str:
    list_1 = []
    for el in list_in:
        rub = int(el)
        cop = int((el * 100) % 100)
        list_1.append(f'{rub:02}  руб {cop:02} коп')
    srt_out = ", ".join(list_1)
    return str_out

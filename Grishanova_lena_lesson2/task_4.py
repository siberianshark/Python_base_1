def convert_name_extract(list_in: list) -> list:
    for i in range(len(list_in)):
        list_in[i] = list_in[i].split()
        list_in[i] = f"Привет, {list_in[i][-1].lower().title()}!"


    return  list_in


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшегоо разряда нИКОЛАй', 'директор аэлита']

result = convert_name_extract(my_list)
print(result)
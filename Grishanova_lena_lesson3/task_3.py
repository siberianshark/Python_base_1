def thesarus(*args):
    name_list = [*args]
    dictionary = {}
    for name in name_list:
        name.capitalize()
        capital = name[0]
        if capital in dictionary.keys():
            dictionary[capital].append(name)
        else:
            dict_1 = [name]
            dictionary[capital] = dict_1
        return dictionary


print(thesarus("Иван", "Мария", "Петр", "Илья"))

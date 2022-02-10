from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    list_str = line = line.split(' ')
    return list_str[0], list_str[5][1:]; list_str[6]

list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))

pprint(list_out)
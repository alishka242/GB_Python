def get_uniq_numbers(src: list):
    uniq_n = set()
    tmp = set()

    for el in src:
        if el not in tmp:
            uniq_n.add(el)
        else: 
            uniq_n.discard(el)
        tmp.add(el)

    return [n for n in src if n in uniq_n]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
from operator import countOf
from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as info:
    # if len(argv) == 2:
    #     i = 0
    #     while i < argv[2]:
    #         info.readline()
    #     print(info.read())
    
    # if  is None and  is not None:
    #     i = 0
    #     while i < argv[2]:
    #         info.readline()
    #     print(info.read())
    # elif argv[2] is None:
    #     pass
    # else: 
    #     print(info.read())
    # print(sum(1 for _ in info))
    print(argv[2])
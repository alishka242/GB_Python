from sys import argv

with open('bakery.csv', 'a+', encoding='utf-8') as sum:
    sum.write(f'{argv[1]}\n')
    print('added')
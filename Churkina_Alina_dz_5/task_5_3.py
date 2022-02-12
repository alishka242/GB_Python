tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def check_gen(tutors: list, klasses: list):
    # Лучше способа не придумала :)
    while len(klasses) < len(tutors):
        klasses.append(None)

    for t in tutors:
        k = klasses[tutors.index(t)]
        yield (t, k) 

generator = check_gen(tutors, klasses)

# добавьте здесь доказательство, что создали именно генератор 
print(type(generator))

for _ in range(len(tutors)):
    print(next(generator))
next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
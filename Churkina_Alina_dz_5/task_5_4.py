from time import perf_counter

def get_numbers(src: list):
    #start = perf_counter()
    src_next = (i for i in src)
    next(src_next)
    gen = (n for s, n in zip(src, src_next) if s < n)
    
    #print("\ntime load gen: " + str(perf_counter() - start))
    
    return gen

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(*get_numbers(src))




"""сравниваю со списком, для сравнения нужно  раскоментитьт код"""
# def get_numbers_list(src: list):
#     start = perf_counter()
#     i = 1
#     numbs = []
#     for n in src:
#         #print(i, len(src))
#         if i < len(src) and n < src[i]:
#             numbs.append(src[i])
#         i += 1
#     print("\ntime load list: " + str(perf_counter() - start))
#     return numbs

# print(get_numbers_list(src)) 
import os

file_statistic = {100 : 0, 1000 : 0, 10000 : 0, 100000 : 0}

def update_stat(f_size):
    for k in file_statistic:
        if f_size < k:
            file_statistic.update({k : file_statistic[k] + 1})

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      f_size = os.path.getsize(os.path.join(root, name))
      update_stat(f_size)

print(file_statistic)

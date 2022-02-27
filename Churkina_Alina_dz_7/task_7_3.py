import os

def check_exists(some_d_f):
    if os.path.exists(some_d_f):
        return 1
    return 0
            
def create_dir(dir_name):
    if not check_exists(dir_name):
        os.makedirs(dir_name)
        print(f'Created new dir {dir_name}')

def create_file(list_files, new_d):
    for f in list_files:
        way_to_file = os.path.join(new_d, f)
        if not check_exists(way_to_file):
            n_file = open(way_to_file, 'w+')
            print(f'Created new file: {f}')
            n_file.close()

def create_conf_dir(BASE_DIR, tree_dirs, conf_name, conf_name_plug):
    """Создаем конф дир"""
    """Проверяем не создаваля ли до нас конфиг dir."""
    new_d = conf_name
 
    if check_exists(conf_name):
        os.mkdir(new_d + '_copy')
        new_d = new_d + '_copy'
    else:
        os.mkdir(new_d)

    for dir_name, list_files in tree_dirs.items():
        """Если k == "-", то нужно создать файл если он еще не сущ. Иначе проверить сущ ли дир, создать все необх"""
        next_d = ''
        
        # if dir_name == conf_name_plug and list_files == ['']: 
        #     pass
        if dir_name != conf_name_plug:
            next_d = os.path.join(new_d, dir_name)
            create_dir(next_d)
        if list_files != ['']:
            create_file(list_files, next_d)

    ##print(tree_dirs)
    """Перебираем ключи, проверяем, что директорий из словаря не сущ, создаем дир и файлы."""
    pass

def get_tree_dirs(conf, conf_name, conf_name_plug):
    tree = os.walk(conf_name)
    dict_dirs = {}

    for i in tree:
        """Получаем список путей до конечных дирректорий в файле конф"""
        kid_dir_n_ind = i[0].find(conf) + len(conf) + 1

        if i[0][kid_dir_n_ind:] != '':
            dir_way = i[0][kid_dir_n_ind:]
        else:
            dir_way = conf_name_plug

        """Проверяем есть ли в директории файлы"""
        if i[2]:
            files = i[2]
        else: 
            files = ['']
        
        """Заполняем словарь. Как ключь используем путь до дир, как значения - список имен файлов. 
        Если файлов нет, то в списке будет пустая строка."""
        dict_dirs[dir_way] = files

    return dict_dirs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conf = 'my_project_hw_7_3'
conf_name = os.path.join(BASE_DIR, conf)
conf_name_plug= "-"
tree_dirs = get_tree_dirs(conf, conf_name, conf_name_plug)
##print(create_dir(BASE_DIR, tree_dirs, new_dold))
create_conf_dir(BASE_DIR, tree_dirs, conf_name, conf_name_plug)
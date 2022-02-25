import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
prj_name = 'my_project'
list_dir = ['settings', 'mainapp', 'adminapp', 'authapp']

def create_dir(**dir_names):
    MY_DIR = os.path.join(BASE_DIR, dir_names['pr'])
    
    if dir_names['l_dir']:
        for dir in dir_names['l_dir']:
            dir_kid = os.path.join(MY_DIR, dir)

            if not os.path.exists(dir_kid):
                os.makedirs(dir_kid)
    else: 
        return "List dirs is empty"

    return os.listdir(MY_DIR)

print(create_dir(pr = prj_name, l_dir = list_dir))
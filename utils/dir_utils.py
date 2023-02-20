import os

def is_dir(mypath):
    return os.path.isdir(mypath)


def create_dir(mypath):
    if not is_dir(mypath):
        os.mkdir(mypath)

def create_directory_tree(dir_list):
    for d in dir_list:
        path = os.path.join(*d.split('/')) 
        if not is_dir(path):
            os.makedirs(path, exist_ok=True)

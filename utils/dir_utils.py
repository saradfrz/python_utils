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

def get_files_in_directory(directory_path):
    files = []
    for file_name in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file_name)):
            files.append(file_name)
    return files
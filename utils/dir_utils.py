import os
from .log_utils import debug_log

def is_dir(mypath):
    return os.path.isdir(mypath)



def create_dir(mypath):
    if not is_dir(mypath):
        try: 
            os.mkdir(mypath)
        except Exception as e:
            debug_log(str(e))

def create_directory_tree(directory_tree):
    # directory_tree: list of strings
    pass
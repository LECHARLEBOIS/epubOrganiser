"""
Name: directoryManager.py
Descr.: Module that will allow the creation of new folder on computer
Author: Louis-Eric Charlebois
Last update: 2023-02-24
"""

import os
import shutil

"""
Name: new_directory
Descr.: Create new directory following specific path
In: a path where the folder need to be create, the name of the folder
Out: a new path
"""
def new_directory(path,name):
    current_path = path
    new_folder_name = name
    new_path = os.path.join(current_path, new_folder_name)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

"""
Name: alter_directory
Descr.: Modify the name of a directory
In: the path with the old name, the path with the new name 
"""
def alter_directory(old_name, new_name):
    os.renames(old_name,new_name)

"""
Name: move_file
Descr.: move a file from one place to another
In: the path with the old name, the path with the new name 
"""
def move_file(original_file_path, direction_dir_path):
    shutil.move(original_file_path,direction_dir_path)

"""
Name: find_path
Descr.: find path of specific file
In: the path of a file
"""
def find_path(file_name):
    file_path = os.path.abspath(file_name)
    return file_path



"""
Name: first_file_path
Descr.: find path of first file in a directory
In: the path of a directory
"""
def first_file_path (folder_path):
    folder = folder_path
    files = os.listdir(folder)

    for file in files:
        if os.path.isfile(os.path.join(folder, file)):
            file_path = os.path.join(folder, file)
            return file_path
            break

#new gen commit

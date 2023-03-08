"""
Name: main.py
Descr.: Main file for a book organiser that will find an author
        and organise it in the right folder.
Author: Louis-Eric Charlebois
Last update: 2023-03-01
"""

import directoryManager
import eBook
import os



if __name__ == "__main__":

    directory=""
    new_directory = ""
    exception_directory = "C:\\Users\\louis\\Documents\\epub_trie\\"+"rejectPile"


    while len(directory)!= 0:
        try:
            next_file_path = directoryManager.first_file_path(directory)
            author = eBook.get_author(next_file_path)

            expected_directory="C:\\Users\\louis\\Documents\\epub_trie\\"+author[0]

            if os.path.exists(expected_directory):
                if os.path.exists(expected_directory):
                    epub_title = eBook.get_title(next_file_path)
                    title_directory="C:\\Users\\louis\\Documents\\epub_trie\\"+epub_title
                    directoryManager.new_directory(expected_directory, epub_title)

                    directoryManager.move_file(next_file_path,expected_directory)

            else:
                directoryManager.new_directory(new_directory,author[0])
                directoryManager.move_file(next_file_path, expected_directory)

        except:
            directoryManager.move_file(next_file_path, exception_directory)


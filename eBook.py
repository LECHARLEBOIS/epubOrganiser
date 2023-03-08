"""
Name: eBook.py
Descr.: Python script that defined the class of a book
Author: Louis-Eric Charlebois
Last update: 2023-03-01
"""

from ebooklib import epub


"""
Name: get_author
Descr.: will find the author of an epub document
In: the epub path
out: the author of a epub file
"""
def get_author(epub_path):
    book = epub.read_epub(epub_path)
    metadata = book.get_metadata("DC", "creator")
    if metadata:
        firstname_lastname = metadata[0][0]
        if "," in metadata[0][0]:
                return metadata[0][0]
        elif " " in metadata[0][0]:
            first_name, last_name = firstname_lastname.split()
            lastname_firstname = last_name + ", " + first_name
            return lastname_firstname
        else:
            return metadata[0][0]

    else:
        return "Unknown"

"""
Name: get_title
Descr.: will find the title of an epub document
In: the epub path
out: the title of an epub file
"""
def get_title(epub_path):
    book = epub.read_epub(epub_path)
    metadata = book.get_metadata("DC", "title")

    if metadata:
        return metadata[0][0]
    else:
        return "Unknown"







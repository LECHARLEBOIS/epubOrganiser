import directoryManager


def clean_directory(main_path,destination_path):
    clean_active = True

    while clean_active is True:
        if len(main_path) != 0:
            deepest_path = directoryManager.enter_deepest_directory(main_path)
            first_file = directoryManager.first_file_path(deepest_path)
            if first_file is not None:
                directoryManager.move_file(first_file,destination_path)
                directoryManager.delete_empty_dir(deepest_path)
                continue
        else:
            clean_active = False

test = "C:\\Users\\louis\\OneDrive\\Documents\\Test To empty"
test_direction = "C:\\Users\\louis\\OneDrive\\Documents\\test Direction"

clean_directory(test,test_direction)


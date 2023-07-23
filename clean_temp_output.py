import os
import glob

def delete_files(directory):
    """
    Delete all files in a directory.

    Parameters:
    directory (str): The directory from which to delete all files.

    This function does not delete the directory itself.
    """
    files = glob.glob(os.path.join(directory, '*'))
    for file in files:
        if os.path.isfile(file):
            os.remove(file)

if __name__ == "__main__":
    delete_files("temp")
    delete_files("output")
    print('Clean Done')

import os
import string
import glob


def remove_punctuation(input_string):
    """
    Remove punctuation from a string.

    Parameters:
    input_string (str): The string from which to remove punctuation.

    Returns:
    str: The input_string with all punctuation characters removed.
    """
    # Make a translator object to remove all punctuation
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)


def process_files():
    """
    Process all text files in the "input/blogs" directory.

    For each file, this function removes all punctuation from the content of the file and writes the cleaned content to a new file in the "temp" directory.

    This function creates the "temp" directory if it does not exist. The names of the output files are the same as the names of the input files.
    """
    input_dir = "input/blogs"
    output_dir = "temp"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read all text files from the input directory
    for filepath in glob.glob(os.path.join(input_dir, '*.txt')):
        with open(filepath, 'r', encoding='utf-8') as f:  # specify 'utf-8' encoding
            data = f.read()

        # Remove punctuation from the data
        data = remove_punctuation(data)

        # Write the cleaned data to a new file in the output directory
        output_filepath = os.path.join(output_dir, os.path.basename(filepath))
        with open(output_filepath, 'w', encoding='utf-8') as f:  # specify 'utf-8' encoding
            f.write(data)


if __name__ == "__main__":
    process_files()
    print('Import and Punctuation Done')

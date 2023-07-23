import os
import glob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def remove_stopwords(tokenized_text):
    """
    Remove English stopwords from a list of tokens.

    Parameters:
    tokenized_text (list of str): The list of word tokens from which to remove stopwords.

    Returns:
    list of str: The list of word tokens with all English stopwords removed.
    """
    stop_words = set(stopwords.words('english'))
    return [word for word in tokenized_text if word not in stop_words]


def lemmatize(tokenized_text):
    """
    Lemmatize a list of tokens.

    Parameters:
    tokenized_text (list of str): The list of word tokens to lemmatize.

    Returns:
    list of str: The list of lemmatized word tokens.
    """
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokenized_text]


def process_files():
    """
    Process all text files in the "temp" directory.

    For each file, this function converts all text to lowercase, removes all English stopwords, and lemmatizes the text,
    then writes the processed text to a new file in the "output" directory.

    This function creates the "output" directory if it does not exist. The names of the output files are the same as the names of the input files.
    """
    input_dir = "temp"
    output_dir = "temp"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read all text files from the input directory
    for filepath in glob.glob(os.path.join(input_dir, '*.txt')):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = f.read().lower()  # convert to lowercase

        # Tokenize the text
        tokens = word_tokenize(data)

        # Remove stopwords
        tokens = remove_stopwords(tokens)

        # Lemmatize
        tokens = lemmatize(tokens)

        # Write the processed data to a new file in the output directory
        output_filepath = os.path.join(output_dir, os.path.basename(filepath))
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(' '.join(tokens))


if __name__ == "__main__":
    process_files()
    print('Text Processed Done')


import os
import glob
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


def get_sentiment(text):
    """
    Get the sentiment of a text.

    Parameters:
    text (str): The text for which to get the sentiment.

    Returns:
    float: The sentiment of the text, a number between -1 (most negative) and 1 (most positive).
    """
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['compound']


def assign_sentiments():
    """
    Assign sentiment to each blog post in the "output" directory and write the results to a CSV file.

    This function reads each blog post, calculates the sentiment of the post, and writes the name of the blog post and its sentiment to a CSV file named "sentiments.csv" in the current directory.
    """
    output_dir = "temp"
    output_file = "output/sentiments.csv"

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Blog Name", "Sentiment"])

        # Read all text files from the output directory
        for filepath in glob.glob(os.path.join(output_dir, '*.txt')):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = f.read()

            sentiment = get_sentiment(data)
            writer.writerow([os.path.basename(filepath), sentiment])


if __name__ == "__main__":
    nltk.download('vader_lexicon')
    assign_sentiments()
    print('Assign Sentiment Done')

import import_clean_punck
import process_text
import clean_temp_output
import assign_sentiment

# Step 1 - Import and Clean Punctuations
import_clean_punck.process_files()

# Step 2 - Import and Clean Punctuations
process_text.process_files()

# Step 3 - Assign Sentiment
assign_sentiment.assign_sentiments()

# Clean Up
clean_temp_output.delete_files("temp")
#clean_temp_output.delete_files("output")


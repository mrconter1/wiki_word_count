from datetime import datetime
import re

# Download and use html file from:
# https://WIKI_NAME.org/w/index.php?title=Special:Contributions/USER_NAME&offset=&limit=2500&target=USER_NAME

path_to_html_file = r'PATH_TO_HTML_FILE'

with open(path_to_html_file, 'r') as file:
    data = file.read()

match_splits = data.split('after change">')

byte_changes = []
for match_split in match_splits:
    
    byte_change_temp = match_split.split('<')[0]
    byte_change = byte_change_temp.replace('âˆ’', '-').replace(',', '')
    
    byte_changes.append(byte_change)

total_changes_in_bytes = 0
for byte_change in byte_changes:
    
    if '+' in byte_change:
        total_changes_in_bytes += int(byte_change)
    elif '-' in byte_change:
        total_changes_in_bytes -= int(byte_change)

# From "https://en.wikipedia.org/wiki/Wikipedia:Size_in_volumes"
bytes_per_word = 8.3

current_date = datetime.today().strftime('%Y-%m-%d')
total_number_of_words = round(total_changes_in_bytes/bytes_per_word)

print("Current date: " + current_date)     
print("Total changes in bytes: " + str(total_changes_in_bytes) + " bytes")
print("Current number of words: " + str(total_number_of_words) + " words")


## wiki_word_count

This Python script calculates the total number of bytes and estimated words contributed by a Wikipedia user. It processes the HTML of a user's contribution page to sum up their edits and provide statistics on their overall impact.

## Features

- Calculates total byte changes from a user's Wikipedia contributions
- Estimates the number of words based on byte changes
- Handles both positive and negative contributions
- Provides current date for reference

## Prerequisites

- Python 3.x
- A web browser to download the contribution page HTML

## Usage

1. Download the HTML file of your Wikipedia contributions:
   - Go to `https://WIKI_NAME.org/w/index.php?title=Special:Contributions/USER_NAME&offset=&limit=2500&target=USER_NAME&end=YYYY-MM-DD`
   - Replace `WIKI_NAME` with the Wikipedia language code (e.g., 'en' for English)
   - Replace `USER_NAME` with your Wikipedia username
   - Replace `YYYY-MM-DD` with the end date for contributions (e.g., '2022-09-15')
   - Save the page as an HTML file

2. Update the script:
   - Set `path_to_html_file` to the location of your downloaded HTML file

3. Run the script:
   ```
   python wikipedia_contributions_calculator.py
   ```

4. View the results:
   - The script will output the current date, total changes in bytes, and estimated number of words contributed

## How it Works

1. The script reads the HTML file of your Wikipedia contributions
2. It extracts the byte changes for each edit
3. The changes are summed up, accounting for both additions and subtractions
4. The total byte change is converted to an estimated word count using the ratio of 8.3 bytes per word (based on Wikipedia's own estimation)

## Notes

- The word count is an estimation and may not be exact
- The script assumes the HTML structure of the contributions page remains consistent
- Large-scale edits or non-textual contributions may skew the results

"""

Removing special characters, spaces, regex, etc. from title.akas.tsv to make it suitable for loading into BigQuery
This script reads the title.akas.tsv file, cleans each field, and writes the cleaned data to a new file.
"""


import csv
import re

INPUT = "imdb/data/title.akas.tsv"
OUTPUT = "imdb/data/title.akas.cleaned.tsv"
JUNK = "imdb/data/title.akas.bad_rows.tsv"

EXPECTED_COLS = 9

def clean_field(value):
    if value == r"\N":
        return ""
    # Remove control characters
    value = re.sub(r"[\r\n\t]", " ", value)
    # Collapse multiple spaces
    value = re.sub(r"\s+", " ", value).strip()
    return value

with open(INPUT, "r", encoding="utf-8", errors="replace") as infile, \
     open(OUTPUT, "w", encoding="utf-8", newline="") as outfile, \
     open(JUNK, "w", encoding="utf-8", newline="") as junkfile:

    reader = csv.reader(infile, delimiter="\t")
    writer = csv.writer(outfile, delimiter="\t")
    junk_writer = csv.writer(junkfile, delimiter="\t")

    for row in reader:
        # Fix rows with fewer columns by padding
        if len(row) < EXPECTED_COLS:
            junk_writer.writerow(row)
            row = row + [""] * (EXPECTED_COLS - len(row))

        # Fix rows with too many columns by merging extras
        if len(row) > EXPECTED_COLS:
            junk_writer.writerow(row)
            row = row[:EXPECTED_COLS]

        cleaned = [clean_field(col) for col in row]
        writer.writerow(cleaned)



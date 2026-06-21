
"""
Because of the size of the data in the name.basics.tsv file, we need to split the data into chunks and then process each chunk separately. 
This notebook contains the code to split the data into 5 separate chunks before loading to bigquery data tables. 
Each chunk will contain approximately 1/5 of the total rows in the original file.
"""

import os

input_file = "imdb/data/title.akas.tsv"
num_chunks = 5

# Count total lines
with open(input_file, "r") as f:
    total_lines = sum(1 for _ in f)

lines_per_chunk = total_lines // num_chunks + 1

with open(input_file, "r") as f:
    header = f.readline()  # keep header in all chunks
    for i in range(num_chunks):
        output_file = f"chunk_{i+1}.tsv"
        with open(output_file, "w") as out:
            out.write(header)
            for _ in range(lines_per_chunk):
                line = f.readline()
                if not line:
                    break
                out.write(line)

print("Done splitting into 5 chunks.")
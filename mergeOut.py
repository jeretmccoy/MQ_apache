import re
import glob
from datetime import datetime

# Regular expression to parse the output files
pattern = re.compile(r'([a-zA-Z]+-\d+) Hits: (\d+) Traffic: (\d+)')

# This dictionary will store our combined data
# Key: month-year, Value: {'hits': hits, 'traffic': traffic}
data = {}

# Get a list of all output files
output_files = sorted(glob.glob('output_*.txt'))

for file in output_files:
    with open(file, 'r') as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                month_year, hits, traffic = match.groups()
                hits, traffic = int(hits), int(traffic)

                # If this month-year is already in our data, update the hits and traffic
                if month_year in data:
                    data[month_year]['hits'] += hits
                    data[month_year]['traffic'] += traffic
                # Otherwise, add a new entry for this month-year
                else:
                    data[month_year] = {'hits': hits, 'traffic': traffic}

# Convert month-year string to datetime object for sorting
def to_datetime(month_year_str):
    return datetime.strptime(month_year_str, '%b-%Y')

# Write the combined and sorted data to the master file
with open('master_output.txt', 'w') as master:
    for month_year in sorted(data.keys(), key=to_datetime):
        master.write(f'{month_year} Hits: {data[month_year]["hits"]} Traffic: {data[month_year]["traffic"]}\n')

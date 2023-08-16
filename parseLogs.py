import re

CHUNK_SIZE = 200 * 1024 * 1024  # 200 MB

def extract_data(line):
    """Extract the month-year and traffic from a log entry"""
    # Extract the date (e.g., "03/Jul/2020")
    match = re.search(r'\[(\d+/[a-zA-Z]+/\d+)', line)
    if not match:
        return None, 0

    date = match.group(1)
    month_year = date.split('/')[1] + "-" + date.split('/')[2]

    # Extract bytes sent
    bytes_sent = int(re.search(r' (\d+) "', line).group(1))

    return month_year, bytes_sent

# Counter for the output files
file_counter = 1
# To store the last portion of a chunk which might be incomplete
partial_line = ""

with open('/var/logs/nginx/access.log', 'rb') as f:
    while True:
        # Read a 200MB chunk
        chunk = f.read(CHUNK_SIZE)
        # If we've reached the end of the file, break
        if not chunk:
            break
        # Convert chunk to string, adding any partial line from the previous chunk
        chunk_str = partial_line + chunk.decode(errors='ignore')
        # Split the chunk into lines
        lines = chunk_str.split('\n')
        # The last line could be incomplete, so store it for the next iteration
        partial_line = lines[-1]
        # Remove the partial line from current lines
        lines = lines[:-1]

        # Process lines to get the summary
        summary = {}
        for line in lines:
            month_year, bytes_sent = extract_data(line)
            if month_year:
                summary.setdefault(month_year, {'hits': 0, 'traffic': 0})
                summary[month_year]['hits'] += 1
                summary[month_year]['traffic'] += bytes_sent
        
        # Write to a new txt file
        with open(f'output_{file_counter}.txt', 'w') as out:
            for month_year, data in summary.items():
                out.write(f'{month_year} Hits: {data["hits"]} Traffic: {data["traffic"]}\n')

        file_counter += 1

# If there's any remaining partial_line left, you can process it if required.

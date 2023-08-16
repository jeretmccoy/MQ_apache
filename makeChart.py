import re
from datetime import datetime
import matplotlib.pyplot as plt

# Parse the master output file
dates = []
hits = []
traffic = []

with open('master_output.txt', 'r') as file:
    for line in file:
        match = re.match(r'([a-zA-Z]+-\d+) Hits: (\d+) Traffic: (\d+)', line.strip())
        if match:
            month_year, hit, traff = match.groups()
            dates.append(datetime.strptime(month_year, '%b-%Y'))
            hits.append(int(hit))
            traffic.append(int(traff))

# Plotting Hits vs Date
plt.figure(figsize=(10, 6))
plt.plot(dates, hits, marker='o', color='b', linestyle='-')
plt.title('Hits Over Time')
plt.xlabel('Date')
plt.ylabel('Hits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('hits_over_time.png')
plt.close()

# Plotting Traffic vs Date
plt.figure(figsize=(10, 6))
plt.plot(dates, traffic, marker='o', color='r', linestyle='-')
plt.title('Traffic Over Time')
plt.xlabel('Date')
plt.ylabel('Traffic (Bytes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('traffic_over_time.png')
plt.close()

#!/bin/bash

echo "Unzipping legacy logs"
7z e /var/legacy_logs/apache.access.log.7z

echo "Parsing logs"
python3 parseLogs.py

echo "Merging output"
python3 mergeOut.py

echo "Install matplotlib"
apt install python3-matplotlib

echo "Making plots"
python3 makeChart.py

echo "Creating the new page"

python3 writeIndex.py

CRON1="0 3 * * * python3 /usr/local/apache2/htdocs/parseLogs.py"
CRON2="0 4 * * * python3 /usr/local/apache2/htdocs/mergeOut.py"
CRON3="0 5 * * * python3 /usr/local/apache2/htdocs/makeChart.py"
CRON4="0 6 * * * python3 /usr/local/apache2/htdocs/writeIndex.py"

echo "Creating cron jobs"

(crontab -1 2>/dev/null; echo "$CRON1") | crontab -
(crontab -1 2>/dev/null; echo "$CRON2") | crontab -
(crontab -1 2>/dev/null; echo "$CRON3") | crontab -
(crontab -1 2>/dev/null; echo "$CRON4") | crontab -


echo "Finished"
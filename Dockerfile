# Use the official Apache httpd image as the base image
FROM httpd:2.4

RUN apt-get update && apt-get install -y python3 python3-pip p7zip-full cron
# Set the working directory inside the container to the htdocs directory of Apache
WORKDIR /usr/local/apache2/htdocs/

COPY index.html makeChart.py mergeOut.py stuff.sh parseLogs.py writeIndex.py /usr/local/apache2/htdocs/
COPY legacy_logs/apache.access.log.7z /var/legacy_logs/apache.access.log.7z

# OPTIONAL: If you'd like Apache to display Nginx logs, you can copy them into the htdocs directory
# This is just for illustrative purposes and not recommended for actual deployments
# RUN cp /nginx-logs/access.log /usr/local/apache2/htdocs/
# RUN cp /nginx-logs/error.log /usr/local/apache2/htdocs/




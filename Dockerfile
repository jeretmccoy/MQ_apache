# Use the official Apache httpd image as the base image
FROM httpd:2.4

# Set the working directory inside the container to the htdocs directory of Apache
WORKDIR /usr/local/apache2/htdocs/

COPY index.html /usr/local/apache2/htdocs/

# OPTIONAL: If you'd like Apache to display Nginx logs, you can copy them into the htdocs directory
# This is just for illustrative purposes and not recommended for actual deployments
# RUN cp /nginx-logs/access.log /usr/local/apache2/htdocs/
# RUN cp /nginx-logs/error.log /usr/local/apache2/htdocs/

EXPOSE 7000

CMD ["/usr/bin/supervisord"]

#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership recursively
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0


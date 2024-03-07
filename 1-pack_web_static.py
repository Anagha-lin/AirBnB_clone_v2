#!/usr/bin/python3
"""
A module for creating a .tgz archive using Fabric.
"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """
    Archives the static files into a .tgz file.
    
    Returns:
        str: Path to the generated archive if successful, None otherwise.
    """
    try:
        # Ensure versions folder exists
        if not os.path.isdir("versions"):
            os.mkdir("versions")

        # Create timestamp for the archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Generate archive name
        archive_name = "versions/web_static_{}.tgz".format(timestamp)

        # Compress the web_static folder into a .tgz archive
        print("Packing web_static to {}".format(archive_name))
        local("tar -cvzf {} web_static".format(archive_name))

        # Get the size of the generated archive
        size = os.stat(archive_name).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_name, size))

        return archive_name
    except Exception as e:
        print("An error occurred during compression:", str(e))
        return None

if __name__ == "__main__":
    do_pack()


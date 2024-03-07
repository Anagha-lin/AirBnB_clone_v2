#!/usr/bin/python3
"""
A module for deploying an archive to web servers using Fabric.
"""
import os
from fabric.api import env, put, run, runs_once
from datetime import datetime

# Set the Fabric environment variables
env.hosts = ['xx-web-01', 'xx-web-02']
env.user = 'ubuntu'


@runs_once
def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path (str): Path to the archive file to be deployed.

    Returns:
        bool: True if all operations are successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        print("Archive does not exist:", archive_path)
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the appropriate directory
        archive_name = os.path.basename(archive_path)
        release_folder = '/data/web_static/releases/' + \
            archive_name.split('.')[0]
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, release_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Move the contents of the extracted folder to the release folder
        run('mv {}/web_static/* {}'.format(release_folder, release_folder))

        # Delete the empty web_static directory
        run('rm -rf {}/web_static'.format(release_folder))

        # Delete the existing symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print("New version deployed!")
        return True
    except Exception as e:
        print("An error occurred during deployment:", str(e))
        return False


if __name__ == "__main__":
    # Example usage
    archive_path = "versions/web_static_20170315003959.tgz"
    do_deploy(archive_path)


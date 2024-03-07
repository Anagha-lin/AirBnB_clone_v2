#!/usr/bin/python3
"""
A module for deploying an archive to web servers using Fabric.
"""
import os
from fabric.api import env, runs_once
from datetime import datetime
from fabric.operations import local
from fabric.context_managers import lcd

# Set the Fabric environment variables
env.hosts = ['xx-web-01', 'xx-web-02']
env.user = 'ubuntu'


@runs_once
def do_pack():
    """
    Compresses the web_static folder into a .tgz archive

    Returns:
        (str): Path to the compressed archive if successful, None otherwise
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate timestamp for the archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Compress the web_static folder into a .tgz archive
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        with lcd("web_static"):
            local("tar -cvzf ../{} .".format(archive_name))

        return archive_name
    except Exception as e:
        print("An error occurred during compression:", str(e))
        return None


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


def deploy():
    """
    Creates and distributes an archive to web servers and deploys it.

    Returns:
        bool: True if all operations are successful, False otherwise.
    """
    # Call the do_pack function and store the path of the created archive
    archive_path = do_pack()

    # Return False if no archive has been created
    if not archive_path:
        print("Failed to create archive.")
        return False

    # Call the do_deploy function using the new path of the new archive
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()


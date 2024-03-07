#!/usr/bin/python3
"""
A module for cleaning out-of-date archives using Fabric.
"""
import os
from fabric.api import env, run
from fabric.context_managers import cd

# Set the Fabric environment variables
env.hosts = ['xx-web-01', 'xx-web-02']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): Number of archives to keep (including the most recent).
                      Defaults to 0.

    Returns:
        bool: True if all operations are successful, False otherwise.
    """
    try:
        number = int(number)
        if number < 0:
            print("Invalid number of archives to keep.")
            return False

        # Get list of archives in versions folder
        with cd('/data/web_static/releases'):
            archives = run('ls -t').split('\n')

        # Remove extra archives in versions folder
        if len(archives) > number:
            archives_to_remove = archives[number:]
            for archive in archives_to_remove:
                run('rm -f {}'.format(archive))

        # Get list of archives in /data/web_static/releases folder
        with cd('/data/web_static/releases'):
            archives = run('ls -t').split('\n')

        # Remove extra archives in /data/web_static/releases folder
        if len(archives) > number:
            archives_to_remove = archives[number:]
            for archive in archives_to_remove:
                run('rm -f {}'.format(archive))

        print("Old archives cleaned successfully.")
        return True
    except Exception as e:
        print("An error occurred during cleanup:", str(e))
        return False


if __name__ == "__main__":
    do_clean()


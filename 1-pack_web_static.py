#!/usr/bin/python3
""" Generates a .tgz archive """

from fabric.api import local
from datetime import datetime

dt = datetime.now()


def do_pack():
    """ Packs web_static files """
    fl_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    local('mkdir -p versions')
    cmd = local('tar -cvzf {} web_static'.format(fl_name))

    return fl_name if cmd.succeeded else None

#!/usr/bin/python3
""" distributes an archive to your web server """

from fabric.api import run, env, put
from os.path import exists
import re

env.hosts = ['34.73.198.19', '54.90.192.199']


def do_deploy(archive_path):
    """ Deploys archive """
    if not exists(archive_path):
        return False

    arch_name = re.split('[/.]', archive_path)[1]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(arch_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
            arch_name, arch_name))
        run('rm /tmp/{}.tgz'.format(arch_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(arch_name, arch_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(arch_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(arch_name))

        return True
    except Exception:
        return False

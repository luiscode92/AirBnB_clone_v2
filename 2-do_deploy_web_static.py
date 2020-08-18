#!/usr/bin/python3
""" distributes an archive to your web server """

from fabric.api import run, env, put
from os.path import exists
import re

env.hosts = ['54.90.192.199', '34.73.198.19']


def do_deploy(archive_path):
    """ Deploys archive """
    if exists(archive_path) is False:
        return False

    arch_name = re.split('[/.]', archive_path)[1]
    direc = '/data/web_static/releases'

    stat = True

    upload = put(archive_path, '/tmp/{}.tgz'.format(arch_name))
    if upload.failed:
        stat = False

    di = run(
        'sudo mkdir -p {}/{}/'.format(direc, arch_name))
    if di.failed:
        stat = False

    unp = run(
        'sudo tar -xzf /tmp/{}.tgz -C {}/{}/'
        .format(arch_name, direc, arch_name))
    if unp.failed:
        stat = False

    rem = run('sudo rm /tmp/{}.tgz'.format(arch_name))
    if rem.failed:
        stat = False

    mov = run(
        'sudo mv {}/{}/web_static/* {}/{}/'
        .format(direc, arch_name, direc, arch_name))
    if mov.failed:
        stat = False

    ren = run(
        'sudo rm -rf {}/{}/web_static'.format(direc, arch_name))
    if ren.failed:
        stat = False

    rep = run('sudo rm -rf /data/web_static/current')
    if rep.failed:
        stat = False

    lin = run(
        'sudo ln -s {}/{}/ /data/web_static/current'
        .format(direc, arch_name))
    if lin.failed:
        stat = False

    return stat

import os

from fabric.api import *

#env.hosts = ['ubuntu@10.211.55.6']

# Notes: for the first deployment there are two steps. In the middle you need to manually configure the postgres DB,
# following these instructions: https://help.ubuntu.com/community/PostgreSQL
# If you want celery or PostGIS support you need to uncomment relevant lines. Search for 'PostGIS' and/or 'Celery'
# This script installs web server under user 'ubuntu', installs project and a couple of logs in home dir. Feel free to modify.
# For further deployments after the first one use the following command: deploy

path, project_name = os.path.split(os.getcwd())
git_repo_remote = 'https://github.com/samufuentes/kano-konnect.git'
user = 'ubuntu'

@task
def run_security_updates(): 
    # Update sources and install security upgrades
    sudo("apt-get update")
    sudo("unattended-upgrade")

@task
def install_dependancies():
    # Installation tools
    sudo("apt-get -y install build-essential")
    sudo("apt-get -y install python-dev")
    sudo("apt-get -y install git-core")
    sudo("apt-get -y install python-setuptools")
    sudo("easy_install pip")
    sudo("pip install virtualenv")

    # Web server and services
    sudo("apt-get -y install nginx")
    # Celery
    # sudo("apt-get -y install rabbitmq-server")

    # DB: PostgreSQL
    sudo("apt-get -y install libpq-dev libxml2 libxml2-dev")
    sudo("apt-get -y install postgresql postgresql-contrib postgresql-server-dev-9.3")
    # PostGIS
    # sudo("apt-get -y install postgresql-9.3-postgis-2.1")
    # PgAdmin
    #sudo("apt-get -y install pgadmin3")

@task
def create_env():
    with cd(project_name):
        run("virtualenv env")

@task
def install_requirements():
    with cd(project_name):
        run("env/bin/pip install -r requirements.txt")

@task
def configure_server():
    with cd(project_name):
        sudo("cp production_files/uwsgi.conf /etc/init/uwsgi.conf")
        sudo("cp production_files/nginx_example /etc/nginx/sites-available")
        with settings(warn_only=True):
            sudo("rm /etc/nginx/sites-enabled/default")
            sudo("ln -s /etc/nginx/sites-available/nginx_example /etc/nginx/sites-enabled/nginx_example")
        # Celery
        # sudo("cp production_files/celery.conf /etc/init/celery.conf")

# @task
# def create_static_dir():
#     with settings(warn_only=True):
#         sudo("mkdir /var/www")
#         sudo("mkdir /var/www/static")
#     sudo("chown ubuntu /var/www/static")

@task
def deploy_static():
    with cd(project_name):
        run('env/bin/python manage.py collectstatic -v0 --noinput')

@task
def reload_services():
    sudo("service nginx reload")
    sudo("service uwsgi reload")
    # Celery
    # sudo("service celery restart")

@task
def restart_services():
    sudo("service nginx restart")
    sudo("service uwsgi restart")
    # Celery
    # sudo("service celery restart")

@task
def update_db_schema():
    with cd(project_name):
        run("env/bin/python manage.py syncdb")
        run("env/bin/python manage.py migrate")

@task
def first_deploy():   
    # To avoid password prompt manually add the following to the
    # /etc/sudoers. Use sudo visudo to edit it
    # ubuntu ALL=(ALL) NOPASSWD: ALL
    # If you're working on amazon instance maybe you don't need this
    run_security_updates()
    install_dependancies()
    # Avoid rsa prompt
    with settings(warn_only=True):
        run('mkdir .ssh')
    run('echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config')
    run("git clone %s" %git_repo_remote)
    sudo('sudo -u postgres createdb kano_konnect')
    create_env()
    install_requirements()
    # create_static_dir()
    deploy_static()
    update_db_schema()
    configure_server()
    restart_services()

@task
def pull():
    with cd(project_name):
        run("git pull origin master")

@task
def deploy():
    run_security_updates()
    pull()
    install_requirements()
    deploy_static()
    update_db_schema()
    reload_services()

@task
def auto_deploy():
    local_dir_name = os.path.dirname(os.path.realpath(__file__))
    local("cd %s; git pull origin master" %local_dir_name)
    local("cd %s; env/bin/pip install -r requirements.txt" %local_dir_name)
    local("cd %s; env/bin/python manage.py syncdb" %local_dir_name)
    local("cd %s; env/bin/python manage.py migrate" %local_dir_name)
    local("sudo service nginx reload")
    local("sudo service uwsgi reload")
    # Celery
    # local("sudo service celery restart")

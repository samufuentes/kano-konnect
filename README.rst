Kano Konnect
=====================

Kano Konnect is the hub for contact information, facility management and aggregated reports. The server stack is the following:

* Django 1.6
* uwsgi
* nginx
* PostgreSQL

Installation guide
~~~~~~~~~~~~~~~~~~

Fork the repo. Clone it. Create a virtualenv
Afterwards::

    $ pip install -r requirements.txt
    $ python manage.py syncdb
    $ python manage.py migrate

Remember to track your migrations with south.

Installation production
~~~~~~~~~~~~~~~~~~~~~~~

The fabric script is tested with an Ubuntu 14.04 LTS created in Amazon from an AMI. Previous to running the script you need to obtain the .pem credentials for the remote server. In addition, to avoid password prompt, you might need to manually add the following to the /etc/sudoers of the remote server. Use sudo visudo to edit it::

    ubuntu ALL=(ALL) NOPASSWD: ALL

For security reasons you need to manually define a couple of env variables on the server. They'll get used by these settings::

    SECRET_KEY = get_env_setting('SECRET_KEY')
    'PASSWORD': get_env_setting('DB_PASSWORD')

Before the first deploy you need to get PostgresSQL DB running on the server (https://help.ubuntu.com/community/PostgreSQL). User should be postgres and password can be anything as long as it's the same in the env variable. You can afterwards trigger the first deployment on a new server entering the directory of the project in your local machine and running::

    $ fab first_deploy -i /path/to/your.pem -H user@server

With that you should have a fully configured server. Subsequent deploys go like this::

    $ fab deploy -i /path/to/your.pem -H user@server

Important information
~~~~~~~~~~~~~~~~~~~~~

There are examples of the configuration of the services in the folder "production_files". They use default values that you might want to adapt to your needs.

The Django settings are in DEBUG mode for the moment. Don't run in this mode in production.

Auto-deploy
~~~~~~~~~~~

In addition, this example allows the possibility to connect a github hook to your server for auto-deploy. By default the server will redeploy when the URL /autodeploy/ gets hit. You can configure a github hook to go there after successful merge, for instance. Right now it doesn't authenticate github, i.e. anybody hitting that URL will force a redeploy. If you don't want it, just comment out the corresponding url in urls.py

Integration with travis CI
~~~~~~~~~~~~~~~~~~~~~~~~~~

This repository is integrated with travis CI as an example of how to do it. The latest build status is built-in below:

.. image:: https://travis-ci.org/samufuentes/kano_konnect.svg?branch=master
    :target: https://travis-ci.org/samufuentes/kano_konnect

Example of a simple github flow when developing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Preparation: connect travis to your repo. Connect a github hook for auto-deploy to a staging server. Clone repo locally.

Pull. Create a branch and edit. Pull and merge. Test; if green, push your branch to github and issue a Pull Request. In the PR check the build status from travis; if green, merge into master. Auto-deployment will trigger. Check staging server. If all goes well manually deploy to production as explained above.

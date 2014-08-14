Kano Konnect
=====================

Kano Konnect is the hub for contact information, facility management and aggregated reports. The server stack is the following:

* Django 1.6
* uwsgi
* nginx
* PostgreSQL

Installation guide
~~~~~~~~~~~~~~~~~~

Fork the repo. Clone it.
Afterwards::

    $ python manage.py syncdb
    $ python manage.py migrate

Remember to track your migrations with south.

Installation production
~~~~~~~~~~~~~~~~~~~~~~~

The fabric script is tested with an Ubuntu 14.04 LTS created in Amazon from an AMI. Previous to running the script you need to obtain the .pem credentials for the remote server. In addition, to avoid password prompt, you might need to manually add the following to the /etc/sudoers of the remote server. Use sudo visudo to edit it::

    ubuntu ALL=(ALL) NOPASSWD: ALL

For security reasons you need to manually define the secret key env variable on the server. It'll get used by this setting::

    SECRET_KEY = get_env_setting('SECRET_KEY')

You can trigger the first deployment on a new server entering the directory of the project in your local machine and running::

    $ fab first_deploy_step1 -i /path/to/your.pem -H user@server

Then configure manually the DB according to the following instructions (https://help.ubuntu.com/community/PostgreSQL) and run the next step::

    $ fab first_deploy_step2 -i /path/to/your.pem -H user@server

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

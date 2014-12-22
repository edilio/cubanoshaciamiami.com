from fabric.api import run, env, task, cd, sudo
from fabric.operations import get

"""
pip install fabric

how to run:
fab deploy -H root@www.jedutils.com
"""

ENV_NAME = 'cubanos'

@task
def deploy():
    prob_home = '/var/www/html/websites/cubanoshaciamiami.com'
    with cd(prob_home):
        sudo('git pull')
        run('workon {} && python manage.py collectstatic --noinput'.format(ENV_NAME))
        run('workon {} && python manage.py migrate'.format(ENV_NAME))
        run('workon {} && gunicorn -w 2 -p 8000 -n cubanos cubanoshaciamiami.wsgi:application &'.format(ENV_NAME))
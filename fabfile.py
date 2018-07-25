from fabric.api import *

# user@host list
env.hosts = [
    'pi@rpi1',
    'pi@rpi2',
    'pi@rpi3',
    'pi@rpi4',
]

# Set password for each host:port pair
for host in env.hosts:
    env.passwords[host + ':22'] = 'Raspberry1234'

@parallel
def reboot():
    # reboot hosts
    sudo('shutdown -r now')

@parallel
def shutdown():
    # shutdown hosts
    sudo('shutdown -h now')

@parallel
def update():
    # apt update & apt dist-upgrade hosts
    sudo('apt-get update')
    sudo('apt-get dist-upgrade -y')

@parallel
def setup():
    # setup hosts (install dependencies)
    sudo('apt-get install -y python3-pip')
    sudo('pip3 install rq redis rsa')

@parallel
def upload():
    # upload code to hosts
    put('tasks.py', 'tasks.py')
    put('worker.py', 'worker.py')

@parallel
def start():
    # start worker.py scripts
    run('python3 worker.py')

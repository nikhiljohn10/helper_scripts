#!/usr/bin/python3.5
"""Create a new Django webapp with a virtualenv.  Defaults to
your free domain, the latest version of Django and Python 3.5

Usage:
  new_django_project_in_virtualenv.py [--domain=<domain> --django=<django-version> --python=<python-version>]

Options:
  --domain=<domain>         Domain name, eg www.mydomain.com   [default: your-username.pythonanywhere.com]
  --django=<django-version> Django version, eg "1.11" [default: latest]
  --python=<python-version> Python version, eg "2.7"  [default: 3.5]
"""

from docopt import docopt
import getpass


def create_virtualenv(name, python_version, django_version):
    pass


def start_django_project(domain, virtualenv_path):
    pass


def create_webapp(domain, project_path):
    pass


def main(domain, django_version, python_version):
    if domain == 'your-username.pythonanywhere.com':
        username = getpass.getuser()
        domain = '{}.pythonanywhere.com'.format(username)
    create_virtualenv(domain, python_version, django_version)



if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments['--domain'], arguments['--django'], arguments['--python'])


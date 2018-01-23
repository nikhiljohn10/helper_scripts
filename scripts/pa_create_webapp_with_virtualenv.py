#!/usr/bin/python3.6
"""Create a web app with a virtualenv

- creates a simple hello world web app
- creates a virtualenv for it and links the two
- creates a project folder for it at ~/www.domain-name.com
- sets up a default static files mapping for /static -> ~/domain.com/static

Usage:
  pa_create_webapp_with_virtualenv.py [--domain=<domain> --python=<python-version>] [--nuke]

Options:
  --domain=<domain>         Domain name, eg www.mydomain.com   [default: your-username.pythonanywhere.com]
  --python=<python-version> Python version, eg "2.7"    [default: 3.6]
  --nuke                    *Irrevocably* delete any existing web app config on this domain. Irrevocably.
"""

from docopt import docopt
import getpass
from textwrap import dedent

from pythonanywhere.project import Project
from pythonanywhere.snakesay import snakesay


def main(repo_url, domain, python_version, nuke):
    if domain == 'your-username.pythonanywhere.com':
        username = getpass.getuser().lower()
        domain = f'{username}.pythonanywhere.com'

    project = Project(domain, python_version)
    project.sanity_checks(nuke=nuke)
    project.virtualenv.create(nuke=nuke)
    project.create_webapp(nuke=nuke)
    project.add_static_file_mappings()
    project.webapp.reload()

    print(snakesay(dedent(
        f'''
        All done!
        - Your site is now live at https://{domain}
        - Your web app config screen is here: https://www.pythonanywhere.com/user/{username}/webapps/{domain.replace('.', '_')}
        '''
    )))




if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments['<git-repo-url>'], arguments['--domain'], arguments['--python'], nuke=arguments.get('--nuke'))


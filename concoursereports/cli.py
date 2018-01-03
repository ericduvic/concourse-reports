"""cli.py: a command line interface for Concourse Reports

Primarily, this provides the commands needed for the Concourse Resource.
"""

import sys
import os
import logging
import json
import glob

import click

from .config import ENDPOINT_URL

logger = logging.getLogger('concoursereports')

@click.command()
def concourse_resource_check():
    """Function to check for new versions.

    No-op'd because this resource is not intended to trigger jobs with new versions.
    """
    sys.stdout.write(json.dumps([]))

@click.command()
@click.argument('destination')
def concourse_resource_in(destination):
    """Function to acquire a resource.
    
    No-op'd because this resource is not intended to be used in any jobs/tasks.
    """
    sys.stdout.write(json.dumps({}))

@click.command()
@click.argument('source_location')
def concourse_resourse_out(source_location):
    """"""
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        logger.exception('Unable to parse JSON data')
        raise
    filename = glob.glob(os.path.join(source_location, '*.xml'))[0]

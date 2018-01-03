""""""

from setuptools import setup

setup(
    name='Concourse Reports',
    version='0.0.1',
    description='CLI for concourse resource and web UI for reviewing reports.',
    packages=['concoursereports'],
    install_requires=['click', 'requests', 'sanic'],
    entry_points={
        'console_scripts': [
            'concourse-resource-check=concoursereports.cli:concourse_resource_check',
            'concourse-resource-in=concoursereports.cli:concourse_resource_in',
            'concourse-resource-out=concoursereports.cli:concourse_resource_out',
        ]
    }
)
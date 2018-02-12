""""""

from sanic import Sanic
from sanic.request import json
from sanic.response import html

from jinja2 import Environment, PackageLoader

from .config import HTTP_PORT, STORAGE_LOCATION
from .api import Api

env = Environment(loader=PackageLoader('concoursereports', 'templates'))

app = Sanic(__name__)

@app.route('/')
async def get_index():
    """"""
    api = Api(STORAGE_LOCATION)
    template = env.get_template('index.html')
    return html(template.render(builds=api.reports))

@app.route('/api/v0/builds')
async def get_report_list(parameter_list):
    """List all active JUnit reports"""
    pass

@app.route('/api/v0/builds', methods=['POST'])
async def add_report():
    """Add a JUnit report"""
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=HTTP_PORT)

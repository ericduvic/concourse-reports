""""""

from sanic import Sanic
from sanic.request import json

from .config import HTTP_PORT

app = Sanic()

@app.route('/')
async def get_report_list(parameter_list):
    """List all active junit reports"""
    pass

@app.route('/', methods=['POST'])
async def add_report():
    """"""
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=HTTP_PORT)

""""""

import os

STORAGE_TYPE = os.environ.get('CR_STORAGE_TYPE', 'file')
STORAGE_LOCATION = os.environ.get('CR_STORAGE_LOCATION', '/tmp')

ENDPOINT_URL = os.environ.get('CR_ENDPOINT_URL', 'http://localhost:8080')

HTTP_PORT = os.environ.get('CR_HTTP_PORT', 8080)

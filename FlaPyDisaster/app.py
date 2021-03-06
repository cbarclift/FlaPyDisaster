﻿"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.

"""
from flask import Flask
import ast


app = Flask(__name__)
UPLOAD_FOLDER = r'tmp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
STATIC_FOLDER = r'static/'
app.config['STATIC_FOLDER'] = STATIC_FOLDER

app.config['USER_FOLDER'] = r'users/'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# routes.py after app is created, circular references
# noinspection PyPep8
from routes import *
# noinspection PyPep8
from globes import *
global_init()

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# launch server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    # Some config testing for lists
    style = ast.literal_eval(GlobalConfig.get('DefaultStyles', '0!default'))
    print(style)
    import mapping.gdal_mapping as gdm
    gdm.hello()
    local_only = GlobalConfig.getboolean('ApplicationConfig', 'local_access_only')
    if local_only:
        app.run(HOST, PORT)
    else:
        accept_remote_connection = "0.0.0.0"
        app.run(accept_remote_connection, PORT)


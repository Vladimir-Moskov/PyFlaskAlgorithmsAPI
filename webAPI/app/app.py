"""
   Algorithms Wep API initialization point
   with creation Flask app, set up dashboard and configure logging
"""

import os
from logging.handlers import RotatingFileHandler
import logging

from flask import Flask
from .config import Config

from flask_restful import Api
from flask_cors import CORS


import flask_monitoringdashboard as dashboard

# set up flask application
app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.config['TESTING'] = Config.TESTING


# set up flask_restful over flask application
api = Api(app, prefix=Config.SERVER_NAME_API_APP)

# add CORS for frontend cross domain policy
cors = CORS(app)

# add web monitoring dashboard
if app.config['TESTING'] == False:
    dashboard.bind(app)

# create and set up simple logging
if app.config['TESTING'] == False:
    try:
        if not os.path.exists('logs'):
            os.mkdir('logs')
    except Exception as error:
        print(repr(error))

    file_handler = RotatingFileHandler(Config.LOG_DIRRECTORY, maxBytes=Config.LOG_SIZE,
                                               backupCount=Config.LOG_BACKUP_COUNT)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)

from . import routes



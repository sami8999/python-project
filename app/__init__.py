import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import simfin as sf
from simfin.names import *
import dash_table
from dash.dependencies import Output, Input, State
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required
from config import BaseConfig
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

sf.set_data_dir('~/simfin_data/')
api_key="ZxGEGRnaTpxMF0pbGQ3JLThgqY2HBL17"


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapps(server)
    register_extensions(server)
    register_blueprints(server)

    return server


def register_dashapps(app):
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp1 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/dashboard/',
                         assets_folder=get_root_path(__name__) + '/assets/',
                         meta_tags=[meta_viewport])
    #html.Img(src= dashapp1.get_asset_url('stock-icon.png')) 
    dashapp1.title = 'Financial Statements'

    dashapp1.layout = html.Div(['hello']) 
        



    
    
    

        
        
        
    _protect_dashviews(dashapp1)
def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])


def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(server)
    login.init_app(server)
    login.login_view = 'main.login'
    migrate.init_app(server, db)


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp)

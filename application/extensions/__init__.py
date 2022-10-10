from .init_sqlalchemy import init_database,db
from .init_admin_manager import init_admin_manager

def init_plugs(app):
    init_database(app)
    init_admin_manager(app)

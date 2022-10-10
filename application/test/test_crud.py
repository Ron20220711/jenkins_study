# method one：
# from application.extensions import db
# # from application.models.test import test_table
# from application import create_app
# app = create_app()
# db.drop_all(app=app)

# method two：
from application.extensions import db
from application.models.test import test_table
from application.models.blog import Role,User
from start import app
with app.app_context():
    # db.drop_all()
    # db.create_all()
    test_add

def test_add():
    ro1 = Role(name='admin')
    ro2 = Role(name='fsr')
    ro3 = Role(name='leader')
    db.session.add_all([ro1, ro2, ro3])
    db.session.commit()
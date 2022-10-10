from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.configs import config
from datetime import datetime

app = Flask(__name__)


# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = config.BaseConfig.SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s' % self.name


# class test_table(db.Model):
#     __tablename__ = "test"
#     id = db.Column(db.Integer, primary_key=True, comment="id")
#     name_str = db.Column(db.String(50), nullable=False, comment="名称")
#     name_var = db.Column(db.VARCHAR(50), default="栗子")
#     name_nvar = db.Column(db.NVARCHAR(50))
#     is_deleted = db.Column(db.Boolean, default=True)
#     date = db.Column(db.Date)
#     flo = db.Column(db.Float(10, 2),default=10.0)
#     Flo_c = db.Column(db.FLOAT(10, 2),default=10.0)
#     dec = db.Column(db.DECIMAL(10, 3))
#     created_at = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
#     updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment="修改时间")
#
#     def __repr__(self):
#         return "test table"


if __name__ == '__main__':
    app.run(debug=True)

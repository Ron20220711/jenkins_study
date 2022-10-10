# from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine


def test_sqlalchemy():
    ur = "mssql+pymssql://sa:135781011@127.0.0.1:1433/test"
    e = create_engine(ur)
    res = list(e.connect().execute("select 1"))
    print("aaa")


if __name__ == '__main__':
    test_sqlalchemy()


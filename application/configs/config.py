import logging
import os
from urllib.parse import quote_plus as urlquote


class BaseConfig:
    # JSON配置
    JSON_AS_ASCII = False
    # redis配置
    REDIS_HOST = os.getenv('REDIS_HOST') or "127.0.0.1"
    REDIS_PORT = int(os.getenv('REDIS_PORT') or 6379)
    # mysql 配置
    USERNAME = "sa"
    PASSWORD = 135781011
    HOST = "127.0.0.1"
    PORT = 1433
    DATABASE = "test"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
    # mysql 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mssql+pymssql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8"
    # 默认日志等级
    LOG_LEVEL = logging.WARN
    # 默认邮件配置
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or '123@qq.com'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') or 'XXXXX'  # 生成的授权码
    # 默认发件人的邮箱,这里填写和MAIL_USERNAME一致即可
    MAIL_DEFAULT_SENDER = ('pear admin', os.getenv('MAIL_USERNAME') or '123@qq.com')


class TestingConfig(BaseConfig):
    """ 测试配置 """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # 内存数据库


class DevelopmentConfig(BaseConfig):
    """ 开发配置 """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(BaseConfig):
    """生成环境配置"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 8
    LOG_LEVEL = logging.ERROR


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

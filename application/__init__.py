from flask import Flask
from application.configs.config import config
from application.extensions import init_plugs




def create_app(config_name=None):
    app = Flask(__name__)
    if not config_name:
        config_name = "development"
    # 引入配置
    app.config.from_object(config[config_name])
    # 注册插件
    init_plugs(app)
    # 注册路由
    # init_view(app)
    return app

from flask_admin import expose
from flask_admin import Admin, BaseView

class MyView1(BaseView):
    @expose('/')
    def main(self):
        return self.render('index.html')

def init_admin_manager(app):
    admin = Admin(app, url='/admin', name='test', template_mode='bootstrap3') # flask-admin 相关的视图配置
    # admin.add_view()
    # test
    # admin.add_view(MyView1(name="aaa",category="111"))


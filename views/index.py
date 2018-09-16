import sys
sys.path.append('..')
import tornado.web
import re
import application
class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello world')
class UserRegisterHanlder(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        context={}
        email=self.get_query_argument('email',default=None)
        password=self.get_query_argument('password')
        password_again=self.get_query_argument('password_again')
        if len(password)<8:
            context['password_length_error']='密码至少8个字符'
        if password_again!=password:
            context['password_input error']='两次密码输入不一致'
        else:
            password=hash(password)
            db=application.Application().db
            sql='insert into user (password) values (%s)'
            db.insert(sql,password)





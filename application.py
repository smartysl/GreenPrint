import tornado.web
from views import index
from config import settings
import torndb
class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/',index.MainHandler),
            (r'/user-register',index.UserRegisterHanlder),
            (r'/user-login',index.UserLoginHandler),
            (r'/user-uploadfile',index.UserUploadFileHandler),
        ]
        super(Application,self).__init__(handlers,**settings)
        self.db=torndb.Connection('localhost:3306','typroject',user='ysl',password='ysl123456')
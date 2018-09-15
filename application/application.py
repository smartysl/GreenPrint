import tornado.web
from views import index
from config import settings
import torndb
class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/(\d+)',index.IndexHandler),
        ]
        super(Application,self).__init__(handlers,**settings)
        self.db=torndb.Connection('localhost:3306','learndb',user='ysl',password='ysl123456')
import tornado.web
import config
import os
from models import students
class IndexHandler(tornado.web.RequestHandler):
    def get(self,num,*args,**kwargs):
        self.write('hello'+num)
class upfilehandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html')
    def post(self, *args, **kwargs):
        file=self.request.files
        for input_name in file:
            fileArr=file[input_name]
            for fileobj in fileArr:
                filepath=os.path.join(config.BASE_DIRS,'media/'+fileobj['filename'])
                with open(filepath,'wb') as f:
                    f.write(fileobj['body'])
        self.write('ok')
class sqlHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        student=students(1,'ysl','18')
        student.save()
        self.write('ok')
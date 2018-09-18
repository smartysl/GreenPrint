import os
import base64
BASE_DIRS=os.path.dirname(__file__)
options={
    'port':8080,
}
settings={
    'static_path':os.path.join('static',BASE_DIRS),
    'cookie_secret':base64.b64encode('于轼霖最帅'),
    'template_path':os.path.join(BASE_DIRS,'templates'),
    'debug':True
}
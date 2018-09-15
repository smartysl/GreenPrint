import os
BASE_DIRS=os.path.dirname(__file__)
options={
    'port':8080,
}
settings={
    'static_path':os.path.join('static',BASE_DIRS),
    'template_path':os.path.join(BASE_DIRS,'templates'),
    'debug':True
}
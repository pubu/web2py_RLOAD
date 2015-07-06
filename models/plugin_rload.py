# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Paul Dircksen'
__email__ = 'p.dircksen@googlemail.com'
__copyright__ = 'Copyright(c) 2015'
__license__ = 'MIT'
__version__ = '0.2'
__status__ = 'Prototype'  # possible options: Prototype, Development, Production
from gluon import *
from gluon.compileapp import run_controller_in
from gluon.html import TAG, DIV, URL, SCRIPT, XML
from react import jsx
import subprocess, random, os

def RLOAD(url, mount_point=None, jsx_compile_expire=1, content='bitte warten ...', **attr):
    """  
    LOADs a React.js component into the action's document

    exposed data:
    - cUrl
    - cId
    - viewData
    - modelData

    Args:
        url
        mount_point=None,
        jsx_compile_expire=60, <- Cache für Kompilierte Templates
        content='bitte warten ...',
        attr*
    """
    
    # Element ID (mount_point) zuweisen 
    mount_point = mount_point or 'c' + str(random.random())[2:]
    attr['_id'] = mount_point
    
    """
    JSX in JS umwandeln (react.js)
    """
    jsx_filepath = os.path.join(request.folder, 'views', url)
    js_str = cache.ram(url+'4', lambda: transform_jsx_view(jsx_filepath), time_expire=jsx_compile_expire)
    """
    JSX ENDE
    """
    if '.' in url:
        f, extension = url.rsplit('.', 1)
    
    attr['_data-w2p_react_remote'] = url
    if not mount_point is None:
        if js_str:
            # mit jsx
            # cid einfügen - content id
            js_str = js_str.replace('{{=cid}}', mount_point)
            url = url.replace('.jsx', '.json')
            data_request_url = '/%s/%s' % (request.application, url)
            # replace url
            js_str = js_str.replace('{{=url}}', data_request_url)
            # run controller - get js_str for viewData and model
            pre_js_str = run_web2py_controller(url)
            
            return CAT(DIV(content, **attr), SCRIPT(pre_js_str+''+js_str))
        else:
            return DIV(content, **attr)

def run_web2py_controller(url):
    """
    run Controller using Model
    """
    # get data from function, and add to output
    # TODO: caching
    url_list = url.split('/')
    data = run_controller_in(url_list[0], url_list[1].replace('.json', ''), current.globalenv)
    view_data = XML(response.json(data['data']))

    model_data = '[]'
    if 'model' in data:
        model_data = XML(response.json(data['model']))
    pre_js_str = """var viewData = %(view_data)s;
var modelData = %(model)s;
    """ % dict(view_data=view_data, model=model_data)   

    return pre_js_str          
    
def transform_jsx_view(jsx_filepath):
    """
    web2py .jsx View compilieren 
    und js als String zurückgeben
    """
    js = ''
    if jsx_filepath.endswith('.jsx'):
        # .jsx Datei wird geöffnenet und umgewandelt
        js_filepath = jsx_filepath.replace('.jsx', '.js')
        js = jsx.transform(jsx_filepath)
    return js

# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    return dict()

def comments():
    """
    react.js compenent for view handling
    das MC -> web2py
    
    jsx is in controller/function.jsx
    
    TODO: create decorator for autobinding view extension
    """
    teaser_text = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum"""
    data = [dict(id=no, author='%d) Author Name' % no, text=teaser_text) for no in xrange(1, 1000)]
    return dict(data=data)

def todo_compare():

    return dict()

# Helper for todo app
def get_todo_rows():
	# get todo rows
    todos = db(db.todo.id > 0).select(cacheable=True)

    return todos

def todo():
    """
    Todo with react.js

    MC by web2py
    View -> .jsx

    """
    todos = get_todo_rows()

    # map fieldtypes web2py -> html
    fldType = {
    'string' : 'text',
    'integer' : 'integer',
    'id'    : 'hidden',
    'datetime' : 'date'
    }

    # load db model and translate to modelData json
    model = []
    for f in db.todo.fields:
        fld = db.todo[f]
        if fld.readable and fld.writable:
            fld_type = fldType[fld.type]
            if fld_type != 'hidden':
                # IS_NOT_EMPTY = field is required
                if isinstance(fld.requires, IS_NOT_EMPTY):
                    fld.required = True
                jfld = dict(name=fld.name, label=fld.label, type=fld_type, widget=fld.widget or '', comment=fld.comment, required=fld.required)
                model.append(jfld)

    return dict(model=model, data=todos)


def todo_web2py_way():
    """
    Todo with web2py SQLFORM 
    """
    # form to add todo
    form = SQLFORM(db.todo, formstyle="bootstrap")
    form.process(formname='todo-form')

    # get todo rows
    todos = get_todo_rows()

    return dict(form=form, data=todos)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

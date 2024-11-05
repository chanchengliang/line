from bottle import get, post, run, request
import sys

@get('/')
def index():
    _stderr("/index")
    return "This is api page for processing POSTed messages"

@post('/')
def index():
    _stderr(request.body.getvalue().decode('utf-8'))
    return request.body
myport= 10000 
run(host='0.0.0.0', port = myport, debug=True)
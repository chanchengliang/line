from bottle import get, post, run, request
import sys

@get('/')
def index():
    return "This is api page for processing POSTed messages"

@post('/')
def index():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body
myport= (10000 || 4000)
run(host='0.0.0.0', port = myport, debug=True)
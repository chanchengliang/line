from bottle import get, post, run, request
import sys

@get('/')
def index():
    return "This is api page for processing POSTed messages"

@post('/')
def index():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

run(host='localhost', port=8082, debug=True)
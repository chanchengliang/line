from bottle import get, post, run, request
import sys
import process

@get('/')
def index():
    return "This is api page for processing POSTed messages"

@post('/')
def index():
    print(request.body.getvalue().decode('utf-8'), file=sys.stdout)
    return request.body

print (str(process.env.PORT))

run(host='localhost', port=10000, debug=True)
from bottle import route, run, template, response, error
import argparse


@route('/')
def index():
    # -- adding a header --
    # response.add_header('header_name', 'header_value')
    
    return template('test.html')

# -- adding subsites (127.0.0.1:8888/hello) --
# @route('/hello')
# def hello():
#    return "<h1>Hello World<h1>"

# -- exception handling --
# @error(404)
# def error404(error):
#     return 'nothing here, sorry'


parser = argparse.ArgumentParser(description='get parameters')
parser.add_argument('-p', '--port', help="specify port (default=8888)", default=8888, type=int)
args = vars(parser.parse_args())

port = args['port']

if port < 0 or port > 65535:
    port = 8888

run(host='127.0.0.1', port=port, debug=True)

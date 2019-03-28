from bottle import route, run, template, response, error

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

run(host='127.0.0.1', port=8888, debug=True)
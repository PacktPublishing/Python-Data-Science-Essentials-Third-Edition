from bottle import route, run, template

port = 9099


@route('/personal/<name>')
def homepage(name):
    return template('Hi <b>{{name}}</b>!', name=name)


print("Try going to http://localhost:{}/personal/Tom".format(port))
print("Try going to http://localhost:{}/personal/Carl".format(port))

run(host='localhost', port=port)

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from bottle import run, request, get, response
import numpy as np
import json

port = 9099


@get('/prediction')
def do_prediction():

    pred = {}

    try:
        sample = [float(request.GET.get('sl')),
                  float(request.GET.get('sw')),
                  float(request.GET.get('pl')),
                  float(request.GET.get('pw'))]

        pred['predicted_label'] = iris['target_names'][classifier.predict(np.matrix(sample))[0]]
        pred['status'] = "OK"
    except:
        pred['status'] = "ERROR"

    response.content_type = 'application/json'
    return json.dumps(pred)



iris = load_iris()
classifier = LogisticRegression()
classifier.fit(iris.data, iris.target)


print("Try going to http://localhost:{}/prediction?sl=5.1&sw=3.5&pl=1.4&pw=0.2".format(port))
print("Try going to http://localhost:{}/prediction?sl=A&sw=B&pl=C&pw=D".format(port))
run(host='localhost', port=port)

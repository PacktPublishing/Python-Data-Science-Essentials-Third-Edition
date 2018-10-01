from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from bottle import run, request, get, post
import numpy as np

port = 9099


@get('/predict')
def predict():
    return '''
        <form action="/prediction" method="post">
            Sepal length [cm]: <input name="sl" type="text" /><br/>
            Sepal width [cm]: <input name="sw" type="text" /><br/>
            Petal length [cm]: <input name="pl" type="text" /><br/>
            Petal width [cm]: <input name="pw" type="text" /><br/>
            <input value="Predict" type="submit" />
        </form>
    '''


@post('/prediction')
def do_prediction():

    try:
        sample = [float(request.POST.get('sl')),
                  float(request.POST.get('sw')),
                  float(request.POST.get('pl')),
                  float(request.POST.get('pw'))]

        pred = classifier.predict(np.matrix(sample))[0]
        return "<p>The predictor says it's a <b>{}</b></p>".format(iris['target_names'][pred])
    except:
        return "<p>Error, values should be all numbers</p>"


iris = load_iris()
classifier = LogisticRegression()
classifier.fit(iris.data, iris.target)


print("Try going to http://localhost:{}/predict".format(port))
run(host='localhost', port=port)

# Try insert the following values:
# [ 5.1, 3.5, 1.4, 0.2] -> setosa
# [ 7.0  3.2, 4.7, 1.4] -> versicolor
# [ 6.3, 3.3, 6.0, 2.5] -> virginica

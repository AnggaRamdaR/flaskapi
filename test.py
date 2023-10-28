from flask import Flask, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('test2.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return('Hello')
@app.route('/pred', methods=['POST'])
def pred():
    sex = int(request.form.get('sex'))
    cp = int(request.form.get('cp'))
    chol = int(request.form.get('chol'))
    fbs = int(request.form.get('fbs'))
    restecg = int(request.form.get('restecg'))
    thalach = int(request.form.get('thalach'))
    exang = int(request.form.get('exang'))
    slope = int(request.form.get('slope'))
    ca = int(request.form.get('ca'))
    thal = int(request.form.get('thal'))

    input = np.array([[sex, cp, chol, fbs, restecg, thalach, exang, slope, ca, thal]])
    result = model.predict(input)[0]
    
    return jsonify({'Heart Disease: ':str(result)})
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
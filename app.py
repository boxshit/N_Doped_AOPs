# -*- coding: utf-8 -*-

"""
@author: HZX
@software: PyCharm
@file: app.py
@time:2023/5/9 14:31
Description:
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import xgboost
from data_prepross import code_NP,code_NME,code_ME
import sklearn

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('Web.html')
    else:
        # get data from web
        Tem = request.form.get('temperature')
        Np = code_NP(request.form.get('N percursor'))
        nme = code_NME(request.form.get('Other non-metallic elements'))
        me = code_ME(request.form.get('metallic elements'))
        CO = request.form.get('C/O')
        pdNc = request.form.get('pdN/pdNc')
        gNc = request.form.get('gN/gNc')
        print(Tem, Np, nme, me, CO, pdNc, gNc, "\n", 'data required')
        # model predict
        X = [Tem, Np, nme, me, CO, pdNc, gNc]
        X1 = np.array([float(x) for x in X]).reshape(1, -1)
        y_pred = model.predict(X1)
        print(X1, y_pred)
        if y_pred==[0]:
            out = "Radical"
        if y_pred==[1]:
            out = "Non-radical"
        return render_template('Web.html', pred_value=out)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

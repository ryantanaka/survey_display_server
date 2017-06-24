#!/usr/bin/env python3
from . import core
import flask


# initialize the app.
app = flask.Flask(__name__)

# placeholder landing page.
@app.route('/')
def landing():
    return 'hello world!'


# placeholder callback route.
@app.route('/callback/<survey>', methods = ['GET','POST'])
def callback(survey):
    print('callback: ',survey)
    if flask.request.method == 'GET':
        return core.handle_spec_request(survey)
    else:
        data = flask.request.json
        print('data: ',data)
        core.save_responses(survey,data)
        return flask.jsonify({})


# user survey access route...
@app.route('/surveys/<survey>', methods = ['GET'])
def surveys(survey):
    print('survey-request: ',survey) 
    return core.survey_app(survey,'form')


# building kiosk access route...
@app.route('/kiosks/<survey>',methods=['GET'])
def kiosks(survey):
    return core.survey_app(survey,'kiosk')



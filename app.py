#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# unit api
# Title: 
# Author: Vojtěch Petrásek 
# Generated: 13/04/2022 9:31:26
##################################################

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
import json
import requests
import os
import sys

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/tests', methods=['GET'])
@cross_origin()
def get_tests():
    return("nějaký testy")

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return("hello")

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=4000)

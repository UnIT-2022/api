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
import pymongo
import xmltodict as xml

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

@app.route('/post_test/<controller>/<uuid>', methods=['GET'])
@cross_origin()
def post_test(controller, uuid):
    client = pymongo.MongoClient("mongodb+srv://unit:PYWxif4nXgdu46aZ@cluster0.snfxu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["tests"]
    col = db[controller]

    x = col.find({"_id":uuid})
    count = 0
    for data in x:
        count += 1
        print(data)
    if count != 0:
        return("update")
    else:
        return("created")

@app.route('/post', methods=['GET'])
@cross_origin()
def post():

    with open("PG24A/IL4_PG24A21510A00_FAIL_PART1_04a1dbd7-d657-4078-9df7-aff4f41152aa.xml") as xml_file:
        data_dict = xml.parse(xml_file.read())
        xml_file.close()
    json_data = json.dumps(data_dict, indent=2)
    data = json.loads(json_data)

    client = pymongo.MongoClient("mongodb+srv://unit:PYWxif4nXgdu46aZ@cluster0.snfxu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["tests"]
    col = db[str(data["test_report"]["head"]["product"]["@family"])]

    #test_data = {"_id":(data["test_report"]["head"]["product"]["@sf-sn"]),"tests":data}
    test_data = {"data": data}
    x = col.insert_one(data)
    print(x)

    return("asi ok")

    

@app.route('/get_test/<controller>/<sn>', methods=['GET'])
@cross_origin()
def get_test(controller, sn):

    client = pymongo.MongoClient("mongodb+srv://unit:PYWxif4nXgdu46aZ@cluster0.snfxu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["tests"]
    col = db[controller]

    querry = {"test_report": 
                {"head": 
                    {"product": {
                        "@sf-sn": sn,
                }
                }
            }
        }
    x = col.find()
    out = []
    for data in x:
        out.append(data["_id"])
    

    return(str(out))

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=4000)

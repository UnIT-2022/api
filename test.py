#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo
client = pymongo.MongoClient("mongodb+srv://unit:PYWxif4nXgdu46aZ@cluster0.snfxu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["tests"]
col = db["IL4"]
test = {"test_report": 
            {"head": 
                {"product": {
                    "@sf-code": "PG24A",
                    "@family": "IL4",
                    "@sf-sn": "21510A00",
                    "@sf-id-string": "PG24ANV21510A00",
                }
                }
            }
        }
x = col.find(test)
x = col.find({},{"test_report": {"head": {"product": {"@sf-sn": "21510A00"}}}})
print("a")
for data in x:
    print(data)
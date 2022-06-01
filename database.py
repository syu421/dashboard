import datetime
from textwrap import indent
from pymongo.mongo_client import MongoClient
import json
from bson.json_util import dumps, loads

def dumpj(dict_sample):
    return dumps(dict_sample, ensure_ascii=False, indent=4, sort_keys=True)

#MongoClient("mongo://username:password@vm-name,ip:port_number")
client = MongoClient("mongodb://study-mongo:study-mongo@study-mongo:27017/")
db = client["shun"] #database
collection = db["gps"] # table

def  post_gps():
    post = {
        "timekey": datetime.datetime.utcnow(),
        "longitude": 35.54279,
        "latitude": 138.8977,
        "gps_number": 11,
        "pdop": 1.22,
        "dimensions": 3,
    }

    result = collection.insert_one(post)
    #print(result.inserted_id)

def get_gps():
    result = collection.find()
    #print(dumpj(result)) # josn変換
    list_result = list(result)
    res = dumps(list_result)
    return res
    #print(list(result)) 
    #reuslt = collection.find_one()
    #print(result)
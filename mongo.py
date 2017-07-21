import json
import pymongo
from pymongo import MongoClient
import requests
from dates import listOfDates

r = requests.get(
    "https://api.tatts.com/sales/vmax/web/data/racing/2017/06/24/sr/full")

# print(r.text)
client = MongoClient('localhost', 27017)
db = client.race_dump_database
COLLECTION = db.ubet_api

RESULT = db.result
RESULT_ID = RESULT.insert_one(r.json()).inserted_id

print(db.collection_names(include_system_collections=False))
CURSOR = db.result.find({})

for item in CURSOR:
    print(item)

#TODO create URL generator

print(listOfDates)

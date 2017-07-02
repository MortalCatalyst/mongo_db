import json
import pymongo
import requests
from pymongo import MongoClient
from dates import listOfDates


r = requests.get("https://api.tatts.com/sales/vmax/web/data/racing/2017/06/24/sr/full")

# print(r.text)
client = MongoClient('localhost', 27017)
db = client.race_dump_database
collection = db.ubet_api

result = db.result
result_id = result.insert_one(r.json()).inserted_id
result_id

print(db.collection_names(include_system_collections=False))
cursor = db.result.find({})

for item in cursor:
    print(item)

#TODO create URL generator

print(listOfDates)

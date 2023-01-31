from flask import Flask, jsonify, request
from pymongo import MongoClient
import json
import requests

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://pyproject:pyproject@cluster0.a0k8jjd.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client

app = Flask(__name__)

print("hello111111")
dbname = get_database()
# Create a new collection
mydbname = dbname["students"]
mycollection = mydbname["student_details"]

# item_details = mycollection.find().sort("name", -1)
my_query = {"name": "Milinda"}
find_doc = mycollection.find(my_query)
for x in find_doc:
    print(x)


@app.post('/addstudentparam')
def addstudentparam():
    try:
        data_to_add = request.json['name']
        # data_to_add = {'name': 'Udani'}
        result = mycollection.insert_one({'name': data_to_add})
        return json.dumps({"acknowledged": result.acknowledged, "inserted_id": result.inserted_id}, default=str)
    except Exception as e:
        return e


@app.route('/getstudentdetails')
def getdetails():
    try:
        query = {"name": "Milinda"}
        find_data = mycollection.find(query)
        for x in find_data:
            print(x)
        return find_data
    except Exception as e:
        return e


@app.route('/addstudentdetails', methods=["POST"])
def addstudentdetails():
    try:
        # data_to_add = request.json['name']
        data_to_add = {'name': 'Udani'}
        result = mycollection.insert_one(data_to_add)
        return json.dumps({"acknowledged": result.acknowledged, "inserted_id": result.inserted_id}, default=str)
    except Exception as e:
        return e


@app.route('/updatestudentdetails', methods=["PUT"])
def updatestudentdetails():
    try:
        data_filter = {'name': 'Milinda'}
        # data_to_update = {'name': 'Nimal'}
        data_to_update = {'$set': {'age': '40', 'address': '400 station road'}}
        result = mycollection.update_one(data_filter, data_to_update)
        return "update successful"
    except Exception as e:
        return e


@app.route('/deletestudentdetails', methods=["DELETE"])
def deletestudentdetails():
    try:
        data_filter = {'name': 'Udani'}
        result = mycollection.delete_one(data_filter)
        print(result)
        return "delete successful"
    except Exception as e:
        return e




def bindex():
    return 'This is test service'

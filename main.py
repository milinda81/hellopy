# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
from pymongo import MongoClient
import json




#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#def index():
#    return 'Hello World'

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://pyproject:pyproject@cluster0.a0k8jjd.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')
app = Flask(__name__)

print("hello111111")
dbname = get_database()
# Create a new collection
mydbname = dbname["students"]
mycollection = mydbname["student_details"]


print("hello333333")
#item_details = mycollection.find().sort("name", -1)
my_query = {"name": "Milinda"}
find_doc = mycollection.find(my_query)
for x in find_doc:
    print(x)

print(2)

@app.route('/getstudentdata')
def index():
    my_query1 = {"name": "Udani"}
    find_doc1 = mycollection.find(my_query)
    bytecode = json.dumps(find_doc1).decode('utf-8')
    print(bytecode)
    return bytecode

@app.route('/world')
def bindex():
    return 'Hello World - WORLD'



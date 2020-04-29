import pymongo
from pymongo import MongoClient
from mongoengine import *

from bson import ObjectId

client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://root:pass@localhost:27017')
connect('mongoengine_UmuziProspects', host = 'localhost', port = 27017)

database = client["UmuziProspects"]
dbcollection = database["Visitors"]

visitor_1 = {"visitor_name":"Manuel", "visitor_age":25, 
			"date_of_visit":"27-04-2020", 
			"time_of_visit":"10:06", "visit_assistant":"Layla Mohlala"}

visitor_2 = {"visitor_name":"Solomon", "visitor_age":37, "date_of_visit":"27-04-2020", 
			"time_of_visit":"11:10", "visit_assistant":"Layla Mohlala"}

visitor_3 = {"visitor_name":"Arnold", "visitor_age":19, "date_of_visit":"27-04-2020", 
			"time_of_visit":"14:38", "visit_assistant":"Bheki Zulu"}

visitor_4 = {"visitor_name":"Lerato", "visitor_age":23, "date_of_visit":"27-04-2020",
			"time_of_visit":"17:53", "visit_assistant":"Bheki Zulu"}

visitor_5 = {"visitor_name":"Daniel", "visitor_age":40, "date_of_visit":"27-04-2020",
			"time_of_visit":"20:00", "visit_assistant":"Bheki Zulu"}


visitor_list = [visitor_1, visitor_2, visitor_3, visitor_4, visitor_5]

def create_visitor(collection, data):

	results = collection.insert_many(data)
	return results

'''visits = visitor_list
result = create_visitor(dbcollection)'''

def list_visitors(collection):

	results = list(collection.find())
	return results

'''result = list_visitors(dbcollection)
print(result)'''


def delete_visitor(collection, data):

	results = collection.delete_one(data)
	return results

'''result = delete_visitor(dbcollection, {'visitor_name':'Solomon'})
print(result)'''


def update_visitor(collection, data, new_values):

	results = collection.update_one(data, {'$set': new_values})
	return results

'''result = update_visitor(dbcollection,{'visitor_name':'Manuel'},{'$set':{'visitor_name':'Tebogo'}})
print(result)'''


def visitor_details(collection, data):

	results = collection.find(data)
	for doc in results:
		return doc

	return results

'''result = visitor_details(dbcollection, {"_id":ObjectId("5ea8fd4bc00d2fd864b8b7bb")})
print(result)'''


def delete_all(collection, data):
	results = collection.delete_many(data)
	return results

'''result = delete_all(db, {})
print(result) #nothing printed on display, db.Visitors.count() gives 0 in shell'''
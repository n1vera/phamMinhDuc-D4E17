from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)

shoppe_database = client.get_database('shoppe')
quiz_database = client.get_database('quiz')

quizzes_collection = quiz_database.get_collection('quizzes')
product_collection = shoppe_database.get_collection('products')

# data = list(product_collection.find) # load all data into ram #READ
data=product_collection.find({"name": "sp_"})  # get one data at time
for d in data:
    print(d)
one_data = product_collection.find_one(
    {"name": "sp_1", "category": "dsp_1"})  # find record have name is sp_2 3 queries
print("only one", one_data)


# insert_data = {
#     "name": "sp_3",
#     "category": "dsp_1",
#     "supplier": "ncc_B"
# }

# product_collection.insert_one(insert_data) # CREATE
# product_collection.insert_many([{},{},{}])

# query = {}
# update = {
#     "$set": {
#        "price": 40
#     }
# }

# product_collection.update_many(query, update) # UPDATE

query = {}
quizzes_collection.delete_many(query)
import pymongo


connection_string = "mongodb+srv://adumanaiadmin:5FlfmqTyzVrmBoWP@adumanai.3hgnlwc.mongodb.net/Adumanai?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = client['adumanaiDB']



import os

class Config:
    SECRET_KEY = os.urandom(24)
    MONGO_URI = 'mongodb+srv://adumanaiadmin:5FlfmqTyzVrmBoWP@adumanai.3hgnlwc.mongodb.net/adumanaiDB'
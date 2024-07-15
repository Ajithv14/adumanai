from django.db import models
import json
from .db_connection import db

cakes_collections = db['cakes']

class Cakes(models.Model):
    
    def __init__(self) -> None:
        self.name = models.CharField(max_length=264)
        self.description = models.TextField()
        self.url = models.URLField()

        self.collections = db['cakes']
    def update(self,name,description,url):
        try:
            print(self.collections.insert_one({"name": name,"description": description, "url": url}).inserted_id)
        except:
            print("Object insertion failed.")
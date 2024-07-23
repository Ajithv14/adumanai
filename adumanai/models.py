from datetime import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from adumanai import login_manager
from adumanai import mongo

class User(UserMixin):
    def __init__(self, email, name, password=None, password_hash=None, _id=None):
        self.email = email
        self.name = name
        self.password_hash = password_hash if password_hash else generate_password_hash(password , method='pbkdf2', salt_length=16)

        self._id = _id if _id else ObjectId()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self._id)
    
    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "password_hash": self.password_hash
        }
    
    @staticmethod
    def from_dict(data):
        return User(
            email=data.get('email'),
            name=data.get('name'),
            password_hash=data.get('password_hash'),
            _id=data.get('_id')
        )

@login_manager.user_loader
def load_user(user_id):
    return User.from_dict(mongo.db.users.find_one({'_id': ObjectId(user_id)}))


class Cake:
    def __init__(self, name, description, price, url, belongs_to=None, _id=None):
        self.name = name
        self.description = description
        self.price = price
        self.url = url

        self._id = _id if _id else ObjectId()
        self.belongs_to = belongs_to if belongs_to else ObjectId(current_user.get_id())

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "url": self.url,
            "belongs_to": self.belongs_to
        }
    
    @staticmethod
    def from_dict(data):
        return Cake(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            url=data.get('url'),
            _id=data.get('_id'),
            belongs_to=data.get('belongs_to'),
        )
    
    def __repr__(self):
        return f'This cake[{self.name} costs {self.price} rupees]'
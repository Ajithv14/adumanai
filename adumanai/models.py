"""adumanai.models"""
from bson.objectid import ObjectId
from flask import session
from flask_login import UserMixin, current_user
from adumanai import login_manager
from adumanai import mongo

class User(UserMixin):
    """Users model"""
    def __init__(self, email, name, _id=None):
        self.email = email
        self.name = name
        self._id = _id if _id else ObjectId()
#    
    def get_id(self):
        """get id for login part"""
        return str(self._id)
    
    def to_dict(self):
        """ to dict """
        return {
            "email": self.email,
            "name": self.name,
            "_id": self._id
        }
    
    @staticmethod
    def from_dict(data):
        """ from dict to model """
        return User(
            email=data.get('email'),
            name=data.get('name'),
            _id=data.get('_id')
        )

# @login_manager.user_loader
# def load_user(user_id):
#     """ load user """
#     print(user_id)
#     return User.from_dict(mongo.db.users.find_one({'_id': ObjectId(user_id)}))

@login_manager.user_loader
def load_user(user_id):
    user_info = session.get('user_info')
    if user_info:
        return User.from_dict(mongo.db.users.find_one({'_id': ObjectId(user_id)}))
    return None


class Cake:
    """Cake model """
    def __init__(self, name, description, price, url, belongs_to=None, _id=None):
        self.name = name
        self.description = description
        self.price = price
        self.url = url

        self._id = _id if _id else ObjectId()
        self.belongs_to = belongs_to if belongs_to else ObjectId(current_user.get_id())

    def to_dict(self):
        """ to dict so that we can get from db """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "url": self.url,
            "belongs_to": self.belongs_to
        }
    
    @staticmethod
    def from_dict(data):
        """from dict to db"""
        return Cake(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            url=data.get('url'),
            _id=data.get('_id'),
            belongs_to=data.get('belongs_to'),
        )
    
    def __repr__(self):
        """String form"""
        return f'This cake[{self.name} costs {self.price} rupees]'
    

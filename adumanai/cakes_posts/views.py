"""adumanai.cakes_posts.views"""
from flask import render_template, url_for, flash, Blueprint, redirect
from flask_login import login_required

from bson.objectid import ObjectId
from adumanai import mongo
from adumanai.models import Cake
from adumanai.cakes_posts.forms import CakeForm
from adumanai.cakes_posts.upload_to_s3 import upload_file_to_s3, delete_file_from_s3

cakes = Blueprint('cakes',__name__)


# Upload cake photos

@cakes.route('/create_post', methods = ['GET', 'POST'])
@login_required
def create_post():
    """Creates a post """
    form = CakeForm()

    if form.validate_on_submit():
        name='_'.join(form.name.data.split(' '))+'.jpg'
        cake = Cake(name=form.name.data,
                     description=form.description.data,
                     price=form.price.data,
                     url = upload_file_to_s3(file=form.picture.data,file_name=name.lower())
        )
        mongo.db.cakes.insert_one(cake.to_dict())
        flash("Upload successful")
        return redirect(url_for('core.index'))
    return render_template('create_post.html',form=form)

@cakes.route('/cake/<cake_id>/delete', methods=["POST"])
def delete_cake(cake_id):
    """
    Handle the deletion of a post by its ID.
    """
    pic_name = mongo.db.cakes.find_one({"_id": ObjectId(cake_id)}).get('name')
    pic_name = '_'.join(pic_name.split(' '))+'.jpg'
    mongo.db.cakes.delete_one({"_id": ObjectId(cake_id)})
    delete_file_from_s3(pic_name.lower())
    flash("Your post has been deleted!", "success")
    return redirect(url_for("core.index"))

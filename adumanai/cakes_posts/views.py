from flask import render_template, url_for, flash, request, Blueprint, redirect
from flask_login import login_user, current_user, logout_user, login_required
from adumanai import mongo
from adumanai.models import Cake
from adumanai.cakes_posts.forms import CakeForm

from bson.objectid import ObjectId
from adumanai.cakes_posts.upload_to_s3 import upload_file_to_s3

cakes = Blueprint('cakes',__name__)


# Upload cake photos

@cakes.route('/create_post', methods = ['GET', 'POST'])
@login_required
def create_post():
    form = CakeForm()

    if form.validate_on_submit():
        name='_'.join(form.name.data.split(' '))+'.'+form.picture.data.filename.split('.')[-1]
        cakes = Cake(name=form.name.data,
                     description=form.description.data,
                     price=form.price.data,
                     url = upload_file_to_s3(file=form.picture.data,file_name=name.lower())
        )
        mongo.db.cakes.insert_one(cakes.to_dict())
        flash("Upload successful")
        return redirect(url_for('core.index'))
    return render_template('create_post.html',form=form)

@cakes.route('/cake/<cake_id>/delete', methods=["POST"])
def delete_cake(cake_id):
    """
    Handle the deletion of a post by its ID.
    """
    mongo.db.cakes.delete_one({"_id": ObjectId(cake_id)})
    flash("Your post has been deleted!", "success")
    return redirect(url_for("core.index"))

from src.app import app
from database import db
from flask import request, Response
from bson.json_util import dumps
import numpy as np
import random




@app.route('/labcreate/<name>')
def create_lab(name):
    new_lab={
    'Title':name}
    result = db.pulls.insert_one(new_lab)
    return {'_id': str(result.inserted_id)} 
   

@app.route("/lab/<Title>/meme")
def random_meme(Title):
    result = random.choice(db.pulls.find({"Lab":Title},{'Url':1}))
    return result
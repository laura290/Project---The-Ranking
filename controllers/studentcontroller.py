from src.app import app
from database import db
from flask import request, Response
from bson.json_util import dumps



@app.route('/')
def welcome():
    return 'Bienvenido!'



@app.route('/studentcreate/<name>')
def create_student(name):
    new_student = {
    'Usuario': name}
    result = db.pulls.insert_one(new_student)
    return {'_id': str(result.inserted_id)}

@app.route('/student/all')
def allstudents():
    result = db.pulls.distinct("Usuario")
    return dumps(result)






 
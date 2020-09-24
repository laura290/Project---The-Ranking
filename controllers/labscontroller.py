
@app.route('/')
def welcome():
    return 'Bienvenido!'


@app.route('/labcreate/<name>')
def create_student(name):
    new_lab = {
    'Title': name}
    result = db.pulls.insert_one(new_student)
    return {'_id': str(result.inserted_id)} 

@app.route("/lab/<Title>/meme")
def random_meme(Title):
    result = random.choice(db.pull_request.find({"Lab":Title},{'Url':1}))
    return result
from flask import Flask
app = Flask("project")

@app.route('/')
def hello_world():
    return 'Hello, World!'
    





from app.GetUserId import *
from app.GetNumberOfPublications import *
from app.GetUserPublications import *
from app.GetUserInfo import *
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello():
    return "True", {'Access-Control-Allow-Origin': '*'}

@app.route('/user', methods=['GET']) #?surname&name
def getUser():
    print("Get user data started")
    if 'name' and 'surname' in request.args:
        surname = request.args['surname']
        name = request.args['name']
        getUserInfoInstance = GetUserInfo(surname, name)
        data = getUserInfoInstance.getInfo()
        print("Get user finished")
        return data, {'Access-Control-Allow-Origin': '*'} 
    else:
        return 'Something went wrong', {'Access-Control-Allow-Origin': '*'}

    
    
if __name__ == "__main__":
    app.run()
        
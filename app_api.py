import sql02
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import senser_sql 

app = Flask(__name__)
CORS(app)
api = Api(app)



class User(Resource):
    def get(self):
        res=sql02.get_sql()
        return res
class Env(Resource):
    def get(self):
        res1=senser_sql.get_sql()
        return res1

api.add_resource(User, '/sql')
api.add_resource(Env, '/env')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8087)

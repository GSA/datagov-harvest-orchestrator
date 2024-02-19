from flask import Flask, request, jsonify
import sys
##from harvester.database.interface import HarvesterDBInterface
#from harvester.database import init_db
#from tests.database.data import new_source, new_job, new_error

app = Flask(__name__)
#db = HarvesterDBInterface()

@app.route('/', methods=['GET'])
def index():
  return "hello : test program"



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True,port=8080)
import json
from Langauge_Model import languageModel as langMod
from Langauge_Model import parshingJSON as pharser
import markdown
import os
from flask_cors import CORS, cross_origin

#import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)
CORS(app)
# Create the API
api = Api(app)
'''
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db
'''
@app.teardown_appcontext
#@cross_origin()
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class GenerateArticle(Resource):
    def get(self):
        return {'message': 'Ready'}, 200

    def post(self):
        '''
        "topic":"posyandu","when":"65 Juni 2020",
        "what":"pelayanan rutin",
        "who":"Pemda Kebumen, pengurus posyandu Buayan, dan warga dusun Jeruk",
        "where":"balai desa pakuran",
        "why":"meningkatkan dayatahan didup balita"
        '''
        parser = reqparse.RequestParser()

        parser.add_argument('topic', required=True)
        parser.add_argument('when', required=True)
        parser.add_argument('what', required=True)
        parser.add_argument('who', required=True)
        parser.add_argument('where', required=True)
        parser.add_argument('why', required=True)
        
        args = parser.parse_args()
        #print(type(args))
        #print(args['topic'])
        #print(type(args))
        the_json = json.dumps(args)
        print(the_json)

        result1,result2,result3=langMod.do_run(the_json)
        '''
        final=pharser.JSONing(result1,result2,result3)
        finalByte = str(final).encode("ASCII", "ignore")
        final = bytes(final, 'utf-8')
        print(type(final))
        '''
        #return "ok"

        #final = final.replace('\"','"')


        #return {"respond": bytes(finalByte)}, 201
        return {"p1":result1,"p2":result2,"p3":result3}, 200



api.add_resource(GenerateArticle, '/generate')


from classes.api import API
from classes.database import Database
from flask import Flask, request
import json

app = Flask(__name__)

# instance DB and API
db = Database()
api = API(db)

@app.route('/api/catalogs/<catalog_id>/prizes', methods=['GET'])
def get_prizes(catalog_id):
    filter = request.args.get('filter')
    pagination = request.args.get('pagination')

    if filter:
        filter = json.loads(filter)
    
    if pagination:
        pagination = json.loads(pagination)

    return api.list_prizes(catalog_id, filter, pagination)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(debug=True)
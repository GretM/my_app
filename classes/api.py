from flask import jsonify, request
import json

class API:
    def __init__(self, db):
        self.db = db
        # self.catalog_data = [1, 2, 3]
        
    def list_prizes(self, catalog_id, filter=None, pagination=None):
        """
            Receives the parameters and returns the list of prizes.
            @type catalog_id: int
            @type filter: dict
            @type pagination: dict

            Returns prizes_list (json).
        """

        try:
            catalog_id = int(catalog_id)
        except ValueError:
            return jsonify({"error": "Catalog ID must be an integer"}), 400
        
        try:
            if filter is not None:
                filter = dict(filter)     
        except ValueError:
            return jsonify({"error": "Filter error"}), 400
        
        try:
            if pagination is not None:
                pagination = dict(pagination)                
        except ValueError:
            return jsonify({"error": "Pagination error"}), 400 
                       
        # query DB with catalog_id and returns prizes list
        results_prizes = self.db.get_prizes(catalog_id, filter, pagination)
        prizes_list = [{"id": prize.id, "title": prize.title, "description": prize.description, "image": prize.image} for prize in results_prizes]
        total = len(results_prizes)
        results_prizes = {
            "total": total,
            "prizes": prizes_list
        }

        # results_prizes = {
        #     "total": 5,
        #     "prizes": [
        #         {
        #         "id": 1,
        #         "title": "Prize 1",
        #         "description": "Description of prize 1",
        #         "image": "https://example.com/image1.png"
        #         },
        #         {
        #         "id": 2,
        #         "title": "Prize 2",
        #         "description": "Description of prize 2",
        #         "image": "https://example.com/image2.png"
        #         },
        #         {
        #         "id": 3,
        #         "title": "Prize 3",
        #         "description": "Description of prize 3",
        #         "image": "https://example.com/image3.png"
        #         },
        #         {
        #         "id": 4,
        #         "title": "Prize 4",
        #         "description": "Description of prize 4",
        #         "image": "https://example.com/image4.png"
        #         },
        #         {
        #         "id": 5,
        #         "title": "Prize 5",
        #         "description": "Description of prize 5",
        #         "image": "https://example.com/image5.png"
        #         },
        #         {
        #         "id": 6,
        #         "title": "Prize 6",
        #         "description": "Description of prize 6",
        #         "image": "https://example.com/image6.png"
        #         },
        #     ]
        # }
        
        return jsonify(results_prizes), 200

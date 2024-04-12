from classes.prize import Prize
# import sqlalchemy

class Database:
    def __init__(self):

        # mock the data instead of connect and execute and query
        self.prizes_data = {
            1: [
                Prize(1, "Prize 1", "Description of prize 1", "https://example.com/image1.png"),
                Prize(2, "Prize 2", "Description of prize 2", "https://example.com/image2.png"),
                Prize(3, "Prize 3", "Description of prize 3", "https://example.com/image3.png"),
                Prize(4, "Prize 4", "Description of prize 4", "https://example.com/image4.png"),
                Prize(5, "Prize 5", "Description of prize 5", "https://example.com/image5.png"),
                Prize(6, "Prize 6", "Description of prize 6", "https://example.com/image6.png"),
                Prize(7, "Prize 7", "Description of prize 7", "https://example.com/image7.png"),
                Prize(8, "Prize 8", "Description of prize 8", "https://example.com/image8.png"),
                Prize(9, "Prize 9", "Description of prize 9", "https://example.com/image9.png"),
                Prize(10, "Prize 10", "Description of prize 10", "https://example.com/image10.png"),
            ],
            2: [
                Prize(11, "Prize 11", "Description of prize 11", "https://example.com/image11.png"),
                Prize(12, "Prize 12", "Description of prize 12", "https://example.com/image12.png"),
                Prize(13, "Prize 13", "Description of prize 13", "https://example.com/image13.png"),
                Prize(14, "Prize 14", "Description of prize 14", "https://example.com/image14.png"),
                Prize(15, "Prize 15", "Description of prize 15", "https://example.com/image15.png"),
                Prize(16, "Prize 16", "Description of prize 16", "https://example.com/image16.png"),
                Prize(17, "Prize 17", "Description of prize 17", "https://example.com/image17.png"),
                Prize(18, "Prize 18", "Description of prize 18", "https://example.com/image18.png"),
                Prize(19, "Prize 19", "Description of prize 19", "https://example.com/image19.png"),
                Prize(20, "Prize 20", "Description of prize 20", "https://example.com/image20.png"),
            ],
        }

    def get_prizes(self, catalog_id, filter=None, pagination=None):
        # query to db and return prizes
        prizes = self.prizes_data.get(int(catalog_id), [])

        # if a filter is provided, it checks if there's a specific ID or description to filter by.
        if filter:
            id_filter = filter['id'] if 'id' in filter else None
            description_filter = filter['description'] if 'description' in filter else None

            if id_filter is not None:
                prizes = [prize for prize in prizes if int(prize.id) == int(id_filter)]

            if description_filter is not None:
                prizes = [prize for prize in prizes if description_filter.lower() in prize.description.lower()]


        if pagination:
            page = int(pagination['page']) if 'page' in pagination else None
            per_page = int(pagination['per_page']) if 'per_page' in pagination else None
            start_index = (page - 1) * per_page
            end_index = start_index + per_page
            prizes = prizes[start_index:end_index]

        return prizes

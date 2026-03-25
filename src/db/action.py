from pymongo import MongoClient


class DB:
    def __init__(self, url: str):
        self.mongoclient = MongoClient(url)

    def ping(self):
        try:
            self.mongoclient.admin.command("ping")
            return True
        except Exception as e:
            return (e, False)

    def insert_data(self, data, db_name: str, collection_name: str):
        try:
            database = self.mongoclient[db_name]
            collection = database[collection_name]
            if isinstance(data, list):
                if not data:
                    return ("No data available to insert.", False)
                insert = collection.insert_many(data)
                return f"Inserted {len(insert.inserted_ids)} documents successfully."

            if isinstance(data, dict):
                insert = collection.insert_one(data)
                return f"Inserted document with _id: {insert.inserted_id}"

            return ("Unsupported data format. Expected dict or list of dicts.", False)
        except Exception as e:
            return (e, False)

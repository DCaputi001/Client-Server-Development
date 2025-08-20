from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user='aacuser', password='password123', host='nv-desktop-services.apporto.com', port=32158):
        """
        Initialize connection to the MongoDB server and select the AAC.animals collection.

        :param user: Username for authentication (default is 'aacuser')
        :param password: Password for authentication
        :param host: MongoDB host address
        :param port: MongoDB connection port
        """
        try:
            self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
            self.database = self.client['AAC']
            self.collection = self.database['animals']
        except PyMongoError as e:
            raise ConnectionError(f"Could not connect to MongoDB: {e}")

    def create(self, data):
        """
        Insert a document into the MongoDB collection.

        :param data: Dictionary containing the document to insert.
        :return: True if insert was successful, otherwise False.
        """
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as e:
                print(f"Insert failed: {e}")
                return False
        else:
            raise ValueError("Data parameter is empty")

    def read(self, query):
        """
        Query documents from the MongoDB collection.

        :param query: Dictionary with key-value pairs for lookup.
        :return: List of documents matching the query, or empty list if none found.
        """
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Read failed: {e}")
            return []

    def update(self, query, update_data):
        """
        Update documents that match the query.

        :param query: Dictionary of fields to match.
        :param update_data: Dictionary with fields to update using $set.
        :return: Number of documents modified.
        """
        if not update_data:
            raise ValueError("Update data cannot be empty.")
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update failed: {e}")
            return 0

    def delete(self, query):
        """
        Delete documents that match the query.

        :param query: Dictionary of fields to match.
        :return: Number of documents deleted.
        """
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete failed: {e}")
            return 0
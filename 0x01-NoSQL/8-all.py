#!/usr/bin/env python3
"""8-all"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.

    Args:
    - mongo_collection: A PyMongo collection object
                        representing the MongoDB collection.

    Returns:
    - A list of documents from the MongoDB collection.
      If the collection is empty, an empty list is returned.
    """
    if not mongo_collection.count_documents({}):
        return []
    return mongo_collection.find()

#!/usr/bin/env python3
"""8-all"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection
    based on provided keyword arguments.

    Args:
    - mongo_collection: A PyMongo collection object representing
                        the MongoDB collection
    - **kwargs: Keyword arguments representing the fields and
                values for the new document

    Returns:
    - The new document's ID (_id) generated by MongoDB
    """
    return mongo_collection.insert(kwargs)

#!/usr/bin/env python3
"""10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field in a document of a MongoDB
    collection based on the provided name.

    Args:
    - mongo_collection: A PyMongo collection object representing
                        the MongoDB collection
    - name: A string representing the name used to identify the
            document to be updated
    - topics: A list of topics to be set in the 'topics' field
              of the identified document

    Returns:
    - None
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})

#!/usr/bin/env python3
"""11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools that have a specific topic.

    Args:
    - mongo_collection: A PyMongo collection object representing
                        the MongoDB collection
    - topic: The specific topic to search for in the 'topics' field

    Returns:
    - A list of schools that have the specified topic
    """
    return mongo_collection.find({"topics": topic})

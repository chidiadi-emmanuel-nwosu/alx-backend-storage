#!/usr/bin/env python3
"""101-students.py"""


def top_students(mongo_collection):
    """
    Updates the 'topics' field in a document of a MongoDB
    collection based on the provided name.

    Args:
    - mongo_collection: A PyMongo collection object representing
                        the MongoDB collection

    Returns:
    - None
    """
    pipeline = [
            {"$unwind": "$topics"},
            {
                "$group": {
                    "_id": "$_id",
                    "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}
                    }
                },
            {"$sort": {"averageScore": -1}}
            ]
    return mongo_collection.aggregate(pipeline)

#!/usr/bin/env python3
"""Module defines `insert_school` function
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document to mongodb database

    Args:
        mongo_collection: A pymongo collection object
        kwargs: dictionary representing the document

    Returns:
        Id of the created document
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id

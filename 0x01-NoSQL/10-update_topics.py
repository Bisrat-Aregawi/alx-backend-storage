#!/usr/bin/env python3
"""Module defines `update_topics` function
"""


def update_topics(mongo_collection, name, topics):
    """Update document with new field

    Args:
        mongo_collection: A pymongo collection object
        name: Name value to query documents
        topics: List of topics to set on document

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

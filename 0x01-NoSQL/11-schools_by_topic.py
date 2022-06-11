#!/usr/bin/env python3
"""Module defines `schools_by_topic` function
"""


def schools_by_topic(mongo_collection, topic):
    """Return list of school docs with specific topic

    Args:
        mongo_collection: A pymongo collection object
        topics: String topic to search

    Returns:
        List of schools
    """
    return mongo_collection.find({"topics": topic})

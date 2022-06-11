#!/usr/bin/env python3
"""Module defines `list-all` function
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in mongodb collection

    Args:
        mongo_collection: A pymongo collection object

    Returns:
        A list of document objects
    """
    return [doc for doc in mongo_collection.find()]

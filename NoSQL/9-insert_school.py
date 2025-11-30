#!/usr/bin/env python3
"""
Module documentation: Inserts a new document into a MongoDB collection.

This module provides a function to insert documents into a MongoDB 
collection using keyword arguments.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    
    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs to be inserted as document fields
        
    Returns:
        ObjectId: the _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

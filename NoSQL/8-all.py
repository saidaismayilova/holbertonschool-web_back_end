#!/usr/bin/env python3
"""
Module documentation: Lists all documents in a MongoDB collection.

This module provides a function to retrieve all documents from a
MongoDB collection using PyMongo.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    Args:
        mongo_collection: pymongo collection object
        
    Returns:
        list: List of all documents in the collection, or empty list if no documents
    """
    return list(mongo_collection.find())

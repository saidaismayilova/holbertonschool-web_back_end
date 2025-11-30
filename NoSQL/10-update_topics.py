#!/usr/bin/env python3
"""
Module documentation: Updates topics of school documents in MongoDB collection.

This module provides a function to update the topics field of school documents
based on the school name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    
    Args:
        mongo_collection: pymongo collection object
        name (str): the school name to update
        topics (list): list of strings representing topics approached in the school
        
    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

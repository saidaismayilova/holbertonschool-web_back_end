#!/usr/bin/env python3
"""
Module documentation: Retrieves schools by specific topic from MongoDB collection.

This module provides a function to find all school documents that contain
a specific topic in their topics field.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    
    Args:
        mongo_collection: pymongo collection object
        topic (str): the topic to search for in school documents
        
    Returns:
        list: list of school documents that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))

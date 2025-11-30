def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    Args:
        mongo_collection: pymongo collection object
        
    Returns:
        list: List of all documents in the collection, or empty list if no documents
    """
    documents = list(mongo_collection.find())
    return documents if documents else []

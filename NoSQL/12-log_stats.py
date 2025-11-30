#!/usr/bin/env python3
"""
Module documentation: Provides statistics about Nginx logs stored in MongoDB.

This script connects to a MongoDB instance and analyzes the nginx collection
in the logs database to provide statistics about HTTP methods and specific
requests like GET /status.
"""


def log_stats():
    """Display statistics about Nginx logs stored in MongoDB."""
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET /status count
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()

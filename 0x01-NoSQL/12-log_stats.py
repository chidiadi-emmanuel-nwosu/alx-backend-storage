#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client: MongoClient = MongoClient('mongodb://127.0.0.1:27017')
    log_collections = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(log_collections.count_documents({}), 'logs')
    print('Methods:')
    for method in methods:
        count = log_collections.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')
    print(f"{log_collections.count_documents({'method': 'GET', 'path': '/status'})} status check")

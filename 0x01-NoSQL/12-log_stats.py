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
        print('    method {}: {}'.format(
            method, log_collections.count_documents({"method": method})))
    print('{} status check'.format(
        log_collections.count_documents({'method': 'GET', 'path': '/status'})))

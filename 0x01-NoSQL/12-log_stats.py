#!/usr/bin/env python3
"""Module summerizes nginx log database
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    logs_count = nginx_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{:d} logs".format(logs_count))
    print("Methods:")
    for method in methods:
        print(
            "\tmethod {:s}: {:d}".format(
                method,
                nginx_collection.count_documents(
                    {"method": method}
                )
            )
        )
    print(
        "{:d} status check".format(
            nginx_collection.count_documents({"path": "/status"})
        )
    )

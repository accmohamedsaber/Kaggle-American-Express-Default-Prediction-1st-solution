from pymongo import MongoClient

def connect_to_mongodb(username, password, host='0.tcp.eu.ngrok.io', port=16936):
    """Connect to MongoDB database with username and password"""
    client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/')
    return client


# Replace USERNAME and PASSWORD with your MongoDB credentials
client = connect_to_mongodb('myUserAdmin', 'giffgaff')


print(client)

print(client.list_database_names())
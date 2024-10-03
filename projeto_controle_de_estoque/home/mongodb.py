from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient('mongodb+srv://rayaneksilva:7iWtMfOxkEMpH869@estoque.he7so.mongodb.net/?retryWrites=true&w=majority&appName=estoque')
    db = client['estoque'] 
    return db

def verify_user(email, password):
    db = connect_to_mongodb()
    users_collection = db['usuarios']
    
    user = users_collection.find_one({'email': email})
    if user and user['senha'] == password:
        return True
    return False

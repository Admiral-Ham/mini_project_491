from schemas.users_schema import User, Transaction
from config.db import db
from pydantic import ValidationError, EmailStr
from datetime import date
import pymongo

users_collections = db.users
transaction_collections = db.transactions

raw_doc = {
        "_id": 1,
        "name": "Test",
        "email": "email123@example.com",
        "password_hash": "hashed_password",
        "creation_time": "2025-9-24",
        "transactions": [],
    }

e1 = {
    "_id": 1,
    "date": "2025-01-01"
}

e2 = {
    
    "date": "2025-01-10"
}
e_list = [e1, e2]

# Test for adding validated transaction
"""try:
    potential_es = Transaction.model_validate(e2)
    print("Transaction created and validated")
    print(f"e2 id = {potential_es.id}")
    inserted_id = transaction_collections.insert_one(potential_es.model_dump(by_alias=True, exclude_none=True)).inserted_id
    print(inserted_id)
except ValidationError as e:
    print("Transaction Doc Invalid")
    print(e)"""

#Test for adding validated user
"""
try:
    #potential_user = User(**raw_doc) #Need to use keyword unpacking to create 
    potential_user = User.model_validate(raw_doc) #Need to use keyword unpacking to create 
    print("User validated and Created")
    print(type(potential_user))

    users_collections.insert_one(potential_user.model_dump(by_alias=True, exclude_none=True))

except ValidationError as e:
    print("User Doc Invalid")
    print(e)

"""


try:
    #raw_user = users_collections.find_one({"_id": 1})
    #p_user = User.model_validate(raw_user)
    new_e = Transaction.model_validate(e2)
    #p_user.transactions.append(new_e)
    print("Successfully added new_transaction to user")
    #updates the transaction array

    #users_collections.update_one(
    #{"_id": 1},
    #{"$set": {"transactions": p_user.model_dump(by_alias=True)["transactions"]}}
    #)

    #users_collections.replace_one({"_id": 1}, p_user.model_dump(by_alias=True, exclude_none=True)) # Replaces entire doc

    #inserts directly into mongodb

    new_e_doc = new_e.model_dump(by_alias=True, exclude_none=True)
    #inserted_id = transaction_collections.insert_one(new_e_doc).inserted_id
    result = users_collections.update_one({"_id": 1}, {"$push": {"transactions":new_e_doc}})

    print("Successfully pushed into db")
except ValidationError as e:
    print("User Doc Invalid")
    print(e)
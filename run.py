from schemas.users_schema import User, Transaction
from config.db import db
from pydantic import ValidationError
from datetime import datetime, timezone
from schemas.helper import convert_mongo_id
from boilerplate import *
from business_service_logic.budget_service import *
from user_services.user_managements import *
from user_services.user_services import *

users_collections = db.users
transaction_collections = db.transactions


def add_user(user):
    try:
        add_user_service(user)
        print("Added user to database")
    except ValidationError as e:
        print("User Doc Invalid")
        print(e)

users_list = []
for x in users:
    users_list.append(x)

#add_user(users_list[0])

"""user_doc = users_collections.find_one({"name": "Alice Johnson"})
user_doc = convert_mongo_id(user_doc)
try:
    valid_user = User.model_validate(user_doc)
    print(valid_user)
except ValidationError as e:
    print("User Doc Invalid")
    print(e)"""

test_user = {
    "name": "TechnicSolutions",
    "email": "TechnicSolutions@example.com",
    "password_hash": "1234",
    "creation_time": datetime(2025, 9, 5, tzinfo=timezone.utc),
    "transactions":[]
}

message = add_user(test_user)
print(message)

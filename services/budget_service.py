from datetime import datetime
from config.db import db
from schemas.budget_schema import Budget
from bson import ObjectId
from schemas.objectID_helper import str_to_object_id

default_categories = ["Needs", "Saves", "Wants"] #business logic

def create_budget(user_id: str, total_amount: float, name : str):
    existing_budget = db.budgets.find_one({"user_id": user_id})
    if existing_budget:
        raise ValueError("Budget already exists for this user")

    budget_document = {
        "user_id": user_id,
        "name": name,
        "total_amount": total_amount,
        "categories": [],
        "created_on": datetime.utcnow(),
    }
    valid_budget_doc = Budget.model_validate(budget_document)
    mongo_budget_doc = valid_budget_doc.model_dump(by_alias=True, exclude_none=True)
    mongo_budget_doc["user_id"] = str_to_object_id(valid_budget_doc["user_id"])
    #if len(budget_document["categories"]) < 1:
    #    raise ValueError("Budget must have at least one category"
    db.budgets.insert_one(budget_document)
    return {"message": "Budget created successfully"}

def get_budget_by_user_id(user_id: str) -> dict:
    """
    Docstring for get_budget_by_user_id
    
    :param user_id: Description
    :type user_id: str
    :return: Description
    :rtype: dict
    """
    user_id_oID = str_to_object_id(user_id)
    return db.budget.find_one(user_id_oID)

def get_budget_by_id(budget_id: ObjectId) -> dict:
    """
    Docstring for get_budget_by_id
    
    :param budget_id: Object ID of Budget Doc
    :type budget_id: ObjectID
    :return: Dictionary belonging to Budget_Id
    :rtype: dict
    """
    return  db.budget.find_one(budget_id)
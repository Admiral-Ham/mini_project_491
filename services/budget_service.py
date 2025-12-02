from datetime import datetime
from config.db import db

default_categories = ["Needs", "Saves", "Wants"] #business logic

def create_budget(user_id, total_amount, name : str, first_time ):
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

    #if len(budget_document["categories"]) < 1:
    #    raise ValueError("Budget must have at least one category"
    db.budgets.insert_one(budget_document)
    return {"message": "Budget created successfully"}


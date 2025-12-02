from config.db import db
from schemas.category_schema import Category as cat
from pydantic import ValidationError

category_collection = db.categories
#Enforces rule number 5, 6, and 7
# Rule #5: category names can be edited
# Rule #6: Category names must be unique
# Rule #7: if a category is deleted, reassign expenses

def add_category_to_budget(user_id: str, category_name: str ):

    budget = db.budgets.find_one({"user_id": user_id})

    category = db.categories.find_one({"user_id" : user_id, 
                                       "name": category_name})
    
    # Checks if the user has a Budget
    if not budget:
        raise ValueError("Budget not found")

    # Rule 6
    if category_name in budget["categories"]:
        raise ValueError("Category already exists")

    db.budgets.update_one({"user_id": user_id},
                          {"$push": {"categories": category_name}}
    )
    return {"message": f"Category '{category_name}' added successfully"}

def rename_category(user_id: str, old_category_name: str, new_category_name: str):
    # Rule 5
    budget = db.budgets.find_one({"user_id": user_id})
    if not budget or old_category_name not in budget["categories"]:
        raise ValueError("Category not found")

    if new_category_name in budget["categories"]:
        raise ValueError("New Category already exists")

    db.budgets.update_one(
        {"user_id": user_id, "categories": old_category_name},
        {"$set: {categories.$": new_category_name}
    )
    return {"message": f"Category '{new_category_name}' renamed successfully"}

def delete_category(user_id, category_name, reassign_to):
    # Rule 7
    db.budgets.update_one(
        {"user_id": user_id},
         {"$pull": {"categories": category_name}}
    )

    # reassign expenses
    db.expenses.update_many(
        {"user_id": user_id, "category": category_name},
        {"$set": {"category": reassign_to}}
    )
    return {"message": f"Category '{category_name}' deleted successfully and reassigned to '{reassign_to}'"}

def create_category(user_id: str, category_name: str, type: str):
    category_doc = {
        "user_id": user_id,
        "name": category_name,
        "type": type
        }
    results = validate_category(category_doc)
    if not results.get("success"):
        return results.get("message")
    return category_collection.insert_one(results)
    

def validate_category(category_data: dict):
    category_doc = {}
    try: 
        category = cat.model_validate(category_data)
        category_doc = category.model_dump(by_alias=True, exclude_none=True)
        return {"success": True, "message":"User validated and created", "return": category_doc}
    except ValidationError as e:
        #print(e)
        return {"success": False,"message":"Missing required fields", "return": category_doc}

def unique_name():
    pass
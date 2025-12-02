from bson import ObjectId

def convert_mongo_id_to_str(doc: dict) -> dict:
    """Convert Mongo's ObjectId `_id` to string so Pydantic can handle it."""
    if doc is None:
        return doc
    doc = dict(doc)  # copy so we don't mutate the original
    if "_id" in doc and isinstance(doc["_id"], ObjectId):
        doc["_id"] = str(doc["_id"])
    return doc
def convert_str_id_to_mongo_id(doc: dict):
    """
    Convert str id to ObjectId to search MongoDB's database
    """
    if doc is None:
        return doc
    doc = dict(doc)  # copy so we don't mutate the original
    if "_id" in doc and isinstance(doc["_id"], str):
        doc["_id"] = ObjectId(doc["_id"])
    return doc
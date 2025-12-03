from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
#from schemas.category_schema import Category
from datetime import datetime

class Budget(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    user_id: str
    name: str = Field(default="Unnamed Budget")
    total_amount: float = Field(default=0)
    categories: List[dict] # Embedded categories of budget
    created_on: datetime

    model_config = {
        "populate_by_name": True,
        "extra": "forbid"
    }

    def validate_budget(doc: dict):
        try: 
            user = Budget.model_validate(doc)
            return True, []
        except ValidationError as e:
            return False, [str(e)]
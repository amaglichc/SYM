from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class TypeEnum(str, Enum):
    salary = "salary"
    investments = "investments"
    other = "other"


class AddIncomeDTO(BaseModel):

    title: str
    coast: Decimal
    type: TypeEnum
    date: datetime


class IncomeDTO(AddIncomeDTO):
    id: int
    creator_id: int
    created_at: datetime

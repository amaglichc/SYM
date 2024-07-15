from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class ExpenseTypeEnum(str, Enum):
    apartment_rent = "Apartment rent"
    groceries = "groceries"
    restaurants = "restaurants"
    sport = "sport"
    subscriptions = "subscriptions"
    furniture = "furniture"
    technique = "technique"
    entertainment = "entertainment"
    medicine = "medicine"
    transport = "transport"
    investment = "investment"


class AddExpenseDTO(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    value: Decimal = Field(gt=0)
    type: ExpenseTypeEnum
    date: datetime


class ExpenseDTO(AddExpenseDTO):
    id: int
    creator_id: int
    created_at: datetime

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.Schemes.ExpenseDTO import ExpenseDTO
from app.Schemes.IncomeDTO import IncomeDTO


class AddUserDTO(BaseModel):
    username: str = Field(min_length=3,max_length=50)
    email: EmailStr
    name: str = Field(min_length=3,max_length=50)
    surname: str | None


class UserDTO(BaseModel):
    id: int
    incomes: list[IncomeDTO] = []
    expenses: list[ExpenseDTO] = []
    created_at: datetime

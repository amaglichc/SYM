from datetime import datetime
from decimal import Decimal

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from app.DB.core import Base
from app.Schemes.IncomeDTO import TypeEnum


class IncomeOrm(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    coast: Mapped[Decimal] = mapped_column(nullable=False)
    type: Mapped[TypeEnum] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(server_default=text("TIMEZONE('utc',now())"))
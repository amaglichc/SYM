from datetime import datetime
from decimal import Decimal

from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.DB.Orms.UserOrm import UserOrm
from app.DB.core import Base
from app.Schemes.IncomeDTO import TypeEnum


class IncomeOrm(Base):
    __tablename__ = "incomes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[Decimal] = mapped_column(nullable=False)
    type: Mapped[TypeEnum] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    creator: Mapped["UserOrm"] = relationship(back_populates="incomes")
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc',now())"))

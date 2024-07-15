from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.DB.core import Base
from app.Schemes.IncomeDTO import IncomeDTO


class UserOrm(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str | None] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    incomes: Mapped[list["IncomeDTO"]] = relationship(
        back_populates="creator",
        cascade="all, delete,save-update"
    )
    expenses: Mapped[list["IncomeDTO"]] = relationship(
        back_populates="creator",
        cascade="all, delete,save-update"
    )

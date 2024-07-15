from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.DB.core import Base
from app.Schemes.IncomeDTO import IncomeDTO


class UserOrm(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str | None] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)
    incomes: Mapped["IncomeDTO"] = relationship(
        back_populates="creater",
        cascade="all, delete,save-update"
    )

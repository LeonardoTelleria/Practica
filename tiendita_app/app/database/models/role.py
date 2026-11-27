from sqlalchemy import Integer, String, Unicode, CheckConstraint
#checkcontrain es una restriccion que podemos hacer
from sqlalchemy.orm import Mapped, mapped_column
from ..engine import Base

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Unicode(200), nullable=True)
    scope: Mapped[str] = mapped_column(String(20), nullable=False)

#argumentos en tabla, osea configurar restricciones en la tabla
    __table_args__ = (
        CheckConstraint(
            "scope IN ('PLATFORM', 'BUSINESS')",
            name="ck_roles_scope"),
    )

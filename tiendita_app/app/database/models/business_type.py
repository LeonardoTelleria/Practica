from sqlalchemy import Integer, String, Unicode, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from ..engine import Base

class BusinessType(Base):
    __tablename__ = "business_types"
    id: Mapped[int] = mapped_column(Integer, primary_key=True) #unicode es para cadenas de texto con caracteres especiales
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(Unicode(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Unicode(250), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

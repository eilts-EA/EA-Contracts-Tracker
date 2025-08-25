import enum
from sqlalchemy import String, Integer, Date, Text, ForeignKey, Numeric, DateTime, func, UniqueConstraint, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Role(str, enum.Enum):
    CONTRACTING_OFFICER = "CONTRACTING_OFFICER"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[Role] = mapped_column(String(32), nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped["DateTime"] = mapped_column(DateTime(timezone=True), server_default=func.now())

class Contract(Base):
    __tablename__ = "contracts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    solicitation_number: Mapped[str | None] = mapped_column(String(128))
    agency: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped["DateTime"] = mapped_column(DateTime(timezone=True), server_default=func.now())
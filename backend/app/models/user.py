from app.db.connection import Base
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(150), nullable= False)
    email: Mapped[str] = mapped_column(String(255), nullable= False, unique= True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable= False)
    created_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= True)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= True)



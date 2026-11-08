from app.db.connection import Base
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Collection_item(Base):
    __tablename__ = "collection_items"

    id: Mapped[int] = mapped_column(primary_key= True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False)
    edition_id: Mapped[int] = mapped_column(ForeignKey("editions.id"), nullable= False)
    created_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= False)
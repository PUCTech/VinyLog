from app.db.connection import Base
from sqlalchemy import ForeignKey, Text, CheckConstraint, UniqueConstraint, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Review(Base):
    __tablename__ = "reviews"

    __table_args__ = (UniqueConstraint("user_id", "album_id", name="unique_user_album_review"), )
    
    id: Mapped[int] = mapped_column(primary_key= True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False)
    album_id: Mapped[int] = mapped_column(ForeignKey ("albums.id"), nullable= False)
    rating: Mapped[int] = mapped_column(CheckConstraint("rating >= 1 AND rating <= 5"),nullable= False)
    review_text: Mapped[str | None] = mapped_column(Text, nullable= True)
    created_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= True)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= True)
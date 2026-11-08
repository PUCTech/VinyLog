from app.db.connection import Base
from sqlalchemy import ForeignKey, Text, UniqueConstraint, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Wishlist(Base):
    __tablename__ = "wishlists"

    __table_args__ = (UniqueConstraint("user_id", "edition_id", name="unique_user_album_review"), )

    id: Mapped[int] = mapped_column(primary_key= True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False)
    edition_id: Mapped[int] = mapped_column(ForeignKey("editions.id"), nullable= False)
    external_url: Mapped[str | None] = mapped_column(Text, nullable= True)
    created_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= True)
        
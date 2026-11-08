from app.db.connection import Base
from sqlalchemy import ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class FavoriteAlbums(Base):
    __tablename__ = "favorite_albums"

    __table_args__ = (UniqueConstraint("user_id", "album_id", name="unique_user_album"), )

    id: Mapped[int] = mapped_column(primary_key= True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"), nullable= False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False)
    created_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= True)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable= True)

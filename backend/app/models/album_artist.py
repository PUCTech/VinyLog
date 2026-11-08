from app.db.connection import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class AlbumArtist(Base):
    __tablename__ = "album_artists"

    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"), primary_key= True, nullable= False)
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"), primary_key= True, nullable= False)
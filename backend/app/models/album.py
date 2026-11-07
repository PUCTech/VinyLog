from app.db.connection import Base
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str] = mapped_column(String(255), nullable= False, unique= False)
    release_year: Mapped[int | None] = mapped_column(nullable= True)
    discogs_master_id: Mapped[int | None] = mapped_column(nullable= True, unique= True)
    metadata_source: Mapped[str | None] = mapped_column(nullable= True)

class AlbumArtist(Base):
    __tablename__ = "album_artists"

    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"), primary_key= True, nullable= False)
    artist_id: Mapped[int] = mapped_column(ForeignKey("artists.id"), primary_key= True, nullable= False)

class FavoriteAlbums(Base):
    __tablename__ = "favorite_albums"

    __table_args__ = (UniqueConstraint("user_id", "album_id", name="unique_user_album_review"), )

    id: Mapped[int] = mapped_column(primary_key= True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"), nullable= False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False)

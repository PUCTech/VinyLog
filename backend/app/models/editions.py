from app.db.connection import Base
from sqlalchemy import String, ForeignKey, CheckConstraint, Text
from sqlalchemy.orm import Mapped, mapped_column

class Edition(Base):
    __tablename__ = "editions"

    id: Mapped[int] = mapped_column(primary_key= True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"), nullable= False)
    discogs_release_id: Mapped[int] = mapped_column(nullable= True)
    edition_name: Mapped[str] = mapped_column(String(255), nullable= True)
    edition_year: Mapped[int] = mapped_column(nullable= True)
    format: Mapped[str] = mapped_column(String(10),CheckConstraint("format IN ('CD', 'VINYL')") ,nullable= False)
    cover_url: Mapped[str] = mapped_column(Text, nullable= False)
from app.db.connection import Base
from sqlalchemy import String, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

class Track(Base):
    __tablename__ = "tracks"

    __table_args__ = (UniqueConstraint("track_number", "edition_id", name="unique_album_track"), )

    id: Mapped[int] = mapped_column(primary_key= True)
    edition_id: Mapped[int] = mapped_column(ForeignKey("editions.id"), nullable= False)
    title: Mapped[str] = mapped_column(String(255), nullable= False)
    track_number: Mapped[int] = mapped_column(CheckConstraint("track_number > 0"), nullable= False)
    duration_seconds: Mapped[int | None] = mapped_column(CheckConstraint("duration_seconds >= 0"),nullable= True)

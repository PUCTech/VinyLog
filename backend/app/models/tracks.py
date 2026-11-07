from app.db.connection import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key= True)
    edition_id: Mapped[int] = mapped_column(ForeignKey("editions.id"), nullable= False)
    title: Mapped[str] = mapped_column(String(255), nullable= False)
    track_number: Mapped[int] = mapped_column(nullable= False)
    duration_seconds: Mapped[int | None] = mapped_column(nullable= True)

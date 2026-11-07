from app.db.connection import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Artist(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(255), nullable= False, unique= False)
    discogs_id: Mapped[int | None] = mapped_column(nullable= True, unique= True)
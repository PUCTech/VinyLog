from app.db.connection import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str] = mapped_column(String(255), nullable= False, unique= False)
    release_year: Mapped[int | None] = mapped_column(nullable= True)
    discogs_master_id: Mapped[int | None] = mapped_column(nullable= True, unique= True)
    metadata_source: Mapped[str | None] = mapped_column(nullable= True)


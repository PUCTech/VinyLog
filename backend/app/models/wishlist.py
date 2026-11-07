from app.db.connection import Base
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

class Wishlist(Base):
    __tablename__ = "wishlists"

    id: Mapped[int] = mapped_column(primary_key= True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable= False)
    edition_id: Mapped[int] = mapped_column(ForeignKey("editions.id"), nullable= False)
    external_url: Mapped[str | None] = mapped_column(Text, nullable= False)
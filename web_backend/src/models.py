from src.database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, text


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

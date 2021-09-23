from sqlalchemy import Column, Integer, String, Text

from app.db.base_class import Base


class Anime(Base):
    id = Column(Integer, primary_key=True, index=True)
    mal_id = Column(Integer, nullable=False)
    url = Column(String(256), nullable=False)
    title = Column(String(256), nullable=True)
    image_url = Column(String(256), nullable=True)
    synopsis = Column(Text(), nullable=True)
    airing_start = Column(String(255), nullable=True)
    episodes = Column(Integer, nullable=True)
    members = Column(Integer, nullable=True)

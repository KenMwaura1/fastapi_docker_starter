from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, index=True)
    mal_id = Column(Integer, unique=True, index=True)
    url = Column(String, index=True)
    title = Column(String, index=True)
    image_url = Column(String)
    synopsis = Column(String)
    type = Column(String)
    airing_start = Column(String)
    episodes = Column(Integer)
    members = Column(Integer)
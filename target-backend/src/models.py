from sqlalchemy import Column, Integer, String
from .database import Base

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String, index=True)
    search_key = Column(String)
    checksum = Column(String)

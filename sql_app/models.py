from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base




class Course(Base):

    __tablename__ = "Course"

    cid = Column(String , primary_key= True)
    cname = Column(String)
    department = Column(String)
    credit = Column(Integer)
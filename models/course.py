from sqlalchemy import Column ,Integer, String
from DB.database import Base


class Course(Base):

    __tablename__ = "Courses"

    CID = Column(String , primary_key= True)
    CourseName = Column(String)
    Department = Column(String)
    Credit = Column(Integer)
from sqlalchemy import Column ,Integer, String
from DB.database import Base



class Student(Base):
    __tablename__ = "Students"

    STID = Column(String , primary_key= True)
    FirstName = Column(String)
    LastName = Column(String)
    FatherName = Column(String)
    DateOfBirth = Column(String)
    IDS = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer)
    CellPhone = Column(String)
    HomePhone = Column(String)
    Department = Column(String)
    Major = Column(String)
    Married = Column(String)
    ID = Column(String)
    SCourseIDs = Column(String)
    LIDs = Column(String)

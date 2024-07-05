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
    LIds = Column(String)





class Professor(Base):
    __tablename__ = "Professors"

    LID = Column(Integer , primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    ID = Column(String)
    Department = Column(String)
    Major = Column(String)
    DateOfBirth = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer)
    CellPhone = Column(String)
    HomePhone = Column(String)
    LCourseIDs= Column(String)





class Course(Base):

    __tablename__ = "Courses"

    CID = Column(String , primary_key= True)
    CourseName = Column(String)
    Department = Column(String)
    Credit = Column(Integer)

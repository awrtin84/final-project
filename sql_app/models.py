from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , VARCHAR
from sql_app.database import Base



#مدل مربوط به دانشجو
class Student(Base):
    __tablename__ = "Students"
    STID = Column(String , primary_key= True)
    FName = Column(String)
    LName = Column(String)
    Father = Column(String)
    Birth = Column(String)
    IDS = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer)
    CPhone = Column(String)
    HPhone = Column(String)
    Department = Column(String)
    Major = Column(String)
    Married = Column(Boolean)
    ID = Column(String)
    SCourseIDs = Column(VARCHAR)
    LIds =  Column(VARCHAR)

    
#-------------------------------------------------------------------------------------------------------------------------------------------
#مدل مربوط به استاد 



class Professor(Base):
    __tablename__ = "Professors"

    LID = Column(Integer , primary_key=True)
    Fname = Column(String)
    Lname = Column(String)
    ID = Column(String)
    Department = Column(String)
    Major = Column(String)
    Birth = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer)
    CPhone = Column(String)
    Hphone = Column(String)
    LCourseIDs = Column(VARCHAR)


#---------------------------------------------------------------------------------------------------------------------------------------------
#مدل مربوط به درس



class Course(Base):

    __tablename__ = "Course"

    CID = Column(String , primary_key= True)
    CName = Column(String)
    Department = Column(String)
    Credit = Column(Integer)
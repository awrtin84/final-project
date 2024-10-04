from sqlalchemy import Column ,Integer, String
from DB.database import Base


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

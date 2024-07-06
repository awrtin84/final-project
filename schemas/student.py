from pydantic import BaseModel


class Student(BaseModel):
    STID : str 
    FirstName : str
    LastName : str
    FatherName : str 
    DateOfBirth : str
    IDS : str
    BornCity : str
    Address : str
    PostalCode : int
    CellPhone : str
    HomePhone : str
    Department : str
    Major : str
    Married : str
    ID : str
    SCourseIDs : str
    LIDs : str

    class Config:
        orm_mode = True

class Student_out(BaseModel):
    FirstName: str
    LastName: str
    STID: str
    ID: str
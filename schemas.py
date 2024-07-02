from pydantic import BaseModel


class Student(BaseModel):
    STID : str 
    FName : str
    LName : str
    Father : str 
    Birth : str
    IDS : str
    BornCity : str
    Address : str
    PostalCode : str
    CPhone : str
    HPhone : str
    Department : str
    Major : str
    Married : str
    ID : str
    SCourseIDs : str
    LIds : str

    class Config:
        orm_mode = True



class Professor(BaseModel):
    LID : str
    Fname : str
    Lname : str
    ID : str 
    Department : str 
    Major : str
    Birth  :str
    BornCity : str 
    Address : str
    PostalCode : int 
    CPhone : str
    Hphone :str
    LCourseIDs : str

    class Config:
        orm_mode = True

class Course(BaseModel):
    CID : str
    CName : str
    Department : str 
    Credit : str 

    class Config:
        orm_mode = True
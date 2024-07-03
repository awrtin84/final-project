from pydantic import BaseModel


class Student(BaseModel):
    STID : str 
    FName : str
    LName : str
    DName : str 
    Birth : str
    IDS : str
    BornCity : str
    Address : str
    PostalCode : int
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
    LID : int
    FName : str
    LName : str
    ID : str 
    Department : str 
    Major : str
    Birth  :str
    BornCity : str 
    Address : str
    PostalCode : int 
    CPhone : str
    HPhone :str
    LCourseIDs : str

    class Config:
        orm_mode = True



class Course(BaseModel):
    CID : str
    CName : str
    Department : str 
    Credit : int

    class Config:
        orm_mode = True
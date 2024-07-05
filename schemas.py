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
    FName: str
    LName: str
    STID: str
    ID: str




class Professor(BaseModel):
    LID : int
    FirstName : str
    LastName : str
    ID : str 
    Department : str 
    Major : str
    DateOfBirth :str
    BornCity : str 
    Address : str
    PostalCode : int 
    CellPhone : str
    HomePhone :str
    LCourseIDs : str

    class Config:
        orm_mode = True



class professor_out(BaseModel):
    Firstname: str
    LastName: str
    ID: str
    DateofBirth: str



    
class Course(BaseModel):
    CID : str
    CourseName : str
    Department : str 
    Credit : int

    class Config:
        orm_mode = True
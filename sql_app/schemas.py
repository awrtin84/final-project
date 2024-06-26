from pydantic import BaseModel, Field

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










class Course(BaseModel):
    Cid : str
    CName : str
    Department : str 
    Credit : int  

class CourseCreate(Course):
    CID : int = Field(title="Course ID" , gt = 0)

class Courseid(Course):
    CID: int

    class Config:
        orm_mode = True
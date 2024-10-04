from pydantic import BaseModel


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
        from_attributes = True


class professor_out(BaseModel):
    FirstName: str
    LastName: str
    ID: str
    DateOfBirth: str
from pydantic import BaseModel


class Course(BaseModel):
    CID : str
    CourseName : str
    Department : str 
    Credit : int

    class Config:
        orm_mode = True
from pydantic import BaseModel


class Course(BaseModel):
    CID : str
    CourseName : str
    Department : str 
    Credit : int

    class Config:
        from_attributes = True
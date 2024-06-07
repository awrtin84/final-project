from typing import Union
from pydantic import BaseModel


class Course(BaseModel):
    cid : str
    cname : str
    department : str 
    credit : int
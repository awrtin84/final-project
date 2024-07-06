from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas import professor as schemas
from DB.crud import professor as P
from DB.crud import course as C
import validation
from depends import get_db

router = APIRouter()




@router.post("/createprofessor/", response_model= schemas.Professor)
def create_professor(professor: schemas.Professor, db: Session = Depends(get_db)):
    
    db_professor = P.get_professor(db, professor.LID)
    if db_professor:
        raise HTTPException(status_code= 400, detail= "!استاد قبلا ثبت شده است")
    validation.validation_professor(professor)
    error_choose_course = {}
    lcourseids = professor.LCourseIDs.split(",")
    for key in lcourseids:
        db_relation_profcourse = C.get_course(db , key)
        if db_relation_profcourse is None:
            error_choose_course["LCourseIDs"]= f'در لیست دروس جدول درس {key} !موجود نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code=400 , detail = error_choose_course)
    return P.create_professor(db= db, professor= professor)


@router.get("/getprofessor/{professor_id}", response_model= schemas.professor_out)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = P.get_professor(db, professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "!استاد یافت نشد")
    return db_professor



@router.put("/professor/{professor_id}", response_model= schemas.Professor)
def update_professor(professor_id: str, professor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = P.update_professor(db, professor_id, professor)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "!استاد یافت نشد")
    validation.validation_professor(professor)
    error_choose_course = {}
    lcourseids = professor.LCourseIDs.split(",")
    for key in lcourseids:
        db_relation_profcourse = C.get_course(db , key)
        if db_relation_profcourse is None:
            error_choose_course["LCourseIDs"]= f'در لیست دروس جدول درس {key} !موجود نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code=400 , detail = error_choose_course)
    return db_professor



@router.delete("/deleteprofessor/{professor_id}", response_model= schemas.professor_out)
def delete_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = P.get_professor(db, professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "!استاد یافت نشد")
    P.delete_professor(db , professor_id)
    return db_professor

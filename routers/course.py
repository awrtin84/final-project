from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from Schemas import course as schemas
from DB.crud import course as crud
from Validations import course as c
from dependency import get_db

router = APIRouter()


#-course--
@router.post("/CreateCourse/", response_model = schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    c.validation_course(course)
    db_course = crud.get_course(db, course.CID)
    if db_course:
        raise HTTPException(status_code=400, detail="!درس قبلا ثبت شده است")
    return crud.create_course(db, course)


@router.get("/getCourse/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if len(str(course_id)) != 5:
        raise HTTPException(status_code= 400, detail=f"نامعتبر می باشد {course_id} !زیرا باید عددی 5 رقمی باشد ")
    if db_course is None:
        raise HTTPException(status_code= 404, detail= " !درس یافت نشد")
    return db_course


@router.put("/updatecourse/{course_id}", response_model=schemas.Course)
def update_course(course_id: str, course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.update_course(db, course_id, course)
    if len(str(course_id)) != 5:
        raise HTTPException(status_code= 400, detail=f"نامعتبر می باشد {course_id} !زیرا باید عددی 5 رقمی باشد ")
    if db_course is None:
        raise HTTPException(status_code=404, detail= "!درس یافت نشد")
    c.validation_course(course)
    return db_course


@router.delete("/deletecourse/{course_id}", response_model= schemas.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if len(str(course_id)) != 5:
        raise HTTPException(status_code= 400, detail=f"نامعتبر می باشد {course_id} !زیرا باید عددی 5 رقمی باشد ")
    if db_course is None:
        raise HTTPException(status_code=404, detail= " !درس یافت نشد")
    crud.delete_course(db, course_id)
    return db_course
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas import student as schemas
from DB.crud import student as S
from DB.crud import course as C
from DB.crud import professor as P
import validation
from dependency import get_db
import re


router = APIRouter()




@router.post("/createstudent/" , response_model = schemas.Student)
def create_student(student: schemas.Student , db: Session = Depends(get_db)):
    db_student = S.get_student(db, student.STID)
    if db_student:
        raise HTTPException(status_code= 400, detail= "!دانشجو قبلا ثبت شده است")
    validation.validation_student(student)
    error_choose_course = {}
    scourseids = student.SCourseIDs.split(",")
    lids = student.LIDs.split(",")
    for key in scourseids:
        db_relation = C.get_course(db , key)
        if db_relation is None:
            error_choose_course["SCourseids"]= f'در لیست دروس جدول درس {key} !موجود نمی باشد'
    for key in lids:
        db_relation_lids = P.get_professor(db , key)
        if db_relation_lids is None:
            error_choose_course["LIDs"]= f'در لیست اساتید جدول درس{key} !موجود نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code= 400 , detail= error_choose_course)
    return S.create_student(db, student)


@router.get("/getstudent/{student_id}" , response_model= schemas.Student_out)
def read_student(student_id: int , db: Session= Depends(get_db)):
    db_student= S.get_student(db , student_id)
    stid_pattern = r"^(400|401|402|403)114150([01-99]{2})$"
    if re.fullmatch(pattern= stid_pattern, string= str(student_id)) == None:
        raise HTTPException(status_code= 400, detail= f'{student_id} !نامعتبر می باشد لطفا دوباره تلاش کنید')
    if db_student is None:
        raise HTTPException(status_code= 404, detail= "!دانشجو یافت نشد")
    return db_student


@router.put("/updatestudent/{student_id}", response_model= schemas.Student)
def update_student(student_id: str, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = S.update_student(db, student_id, student)
    stid_pattern = r"^(400|401|402|403)114150([01-99]{2})$"
    if re.fullmatch(pattern= stid_pattern, string= str(student_id)) == None:
        raise HTTPException(status_code= 400, detail= f'{student_id}!نامعتبر می باشد لطفا دوباره تلاش کنید')
    if db_student is None:
        raise HTTPException(status_code=404, detail= "!دانشجو یافت نشد")
    validation.validation_student(student)
    error_choose_course = {}
    scourseids = student.SCourseIDs.split(",")
    lids = student.LIDs.split(",")
    for key in scourseids:
        db_relation = C.get_course(db , key)
        if db_relation is None:
            error_choose_course["SCourseids"]= f'در لیست دروس جدول درس {key} !موجود نمی باشد'
    for key in lids:
        db_relation_lids = P.get_professor(db , key)
        if db_relation_lids is None:
            error_choose_course["LIDs"]= f'در لیست اساتید جدول درس{key} !موجود نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code= 400 , detail= error_choose_course)
    return db_student

 
@router.delete("/deletestudent/{student_id}", response_model= schemas.Student_out)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = S.get_student(db, student_id)
    stid_pattern = r"^(400|401|402|403)114150([01-99]{2})$"
    if re.fullmatch(pattern= stid_pattern, string= str(student_id)) == None:
        raise HTTPException(status_code= 400, detail= f'{student_id} !نامعتبر می باشد لطفا دوباره تلاش کنید')
    if db_student is None:
        raise HTTPException(status_code= 404, detail= "!دانشجو یافت نشد")
    S.delete_student(db , student_id)
    return db_student
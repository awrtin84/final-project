from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import schemas
from DB import crud, models
from DB.database import SessionLocal, engine
import validation


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#-Student--

@app.post("/createstudent/" , response_model = schemas.Student)
def create_student(student: schemas.Student , db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student.STID)
    if db_student:
        raise HTTPException(status_code= 400, detail= "!دانشجو قبلا ثبت شده است")
    validation.validation_student(student)
    error_choose_course = {}
    scourseids = student.SCourseIDs.split(",")
    lids = student.LIDs.split(",")
    for key in scourseids:
        db_relation = crud.get_course(db , key)
        if db_relation is None:
            error_choose_course["SCourseids"]= '!کد درس انتخاب شده جز دروس جدول درس نمی باشد'
    for key in lids:
        db_relation_lids = crud.get_professor(db , key)
        if db_relation_lids is None:
            error_choose_course["LIDs"]= '!استاد انتخاب شده جز اساتید جدول استاد نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code= 400 , detail= error_choose_course)
    return crud.create_student(db, student)


@app.get("/getstudent/{student_id}" , response_model= schemas.Student_out)
def read_student(student_id: int , db: Session= Depends(get_db)):
    db_student= crud.get_student(db , student_id)
    if db_student is None:
        raise HTTPException(status_code= 404 , detail= "!دانشجو یافت نشد")
    return db_student


@app.put("/updatestudent/{student_id}", response_model= schemas.Student)
def update_student(student_id: str, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail= "!دانشجو یافت نشد")
    validation.validation_student(student)
    error_choose_course = {}
    scourseids = student.SCourseIDs.split(",")
    lids = student.LIDs.split(",")
    for key in scourseids:
        db_relation = crud.get_course(db , key)
        if db_relation is None:
            error_choose_course["SCourseids"]= '!کد درس انتخاب شده جز دروس جدول درس نمی باشد'
    for key in lids:
        db_relation_lids = crud.get_professor(db , key)
        if db_relation_lids is None:
            error_choose_course["LIDs"]= '!استاد انتخاب شده جز اساتید جدول استاد نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code= 400 , detail= error_choose_course)
    return db_student

 
@app.delete("/deletestudent/{student_id}", response_model= schemas.Student_out)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code= 404, detail= "!دانشجو یافت نشد")
    crud.delete_student(db , student_id)
    return db_student
    


#-professor---


@app.post("/createprofessor/", response_model= schemas.Professor)
def create_professor(professor: schemas.Professor, db: Session = Depends(get_db)):
    
    db_professor = crud.get_professor(db, professor.LID)
    if db_professor:
        raise HTTPException(status_code= 400, detail= "!استاد قبلا ثبت شده است")
    validation.validation_professor(professor)
    error_choose_course = {}
    lcourseids = professor.LCourseIDs.split(",")
    for key in lcourseids:
        db_relation_profcourse = crud.get_course(db , key)
        if db_relation_profcourse is None:
            error_choose_course["LCourseIDs"]= '!کد درس در جدول دروس موجود نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code=400 , detail = error_choose_course)
    return crud.create_professor(db= db, professor= professor)


@app.get("/getprofessor/{professor_id}", response_model= schemas.Professor)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "!استاد یافت نشد")
    return db_professor



@app.put("/professor/{professor_id}", response_model= schemas.Professor)
def update_professor(professor_id: str, professor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = crud.update_professor(db, professor_id, professor)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "!استاد یافت نشد")
    validation.validation_professor(professor)
    error_choose_course = {}
    lcourseids = professor.LCourseIDs.split(",")
    for key in lcourseids:
        db_relation_profcourse = crud.get_course(db , key)
        if db_relation_profcourse is None:
            error_choose_course["LCourseIDs"]= '!کد درس در جدول دروس موجود نمی باشد'
    if error_choose_course:
        raise HTTPException(status_code=400 , detail = error_choose_course)
    return db_professor



@app.delete("/deleteprofessor/{professor_id}", response_model= schemas.Professor)
def delete_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "!استاد یافت نشد")
    crud.delete_professor(db , professor_id)
    return db_professor


#-course--
@app.post("/CreateCourse/", response_model = schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    validation.validation_course(course)
    db_course = crud.get_course(db, course_id = course.CID)
    if db_course:
        raise HTTPException(status_code=400, detail="!درس قبلا ثبت شده است")
    return crud.create_course(db, course)


@app.get("/getCourse/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if db_course is None:
        raise HTTPException(status_code= 404, detail= " !درس یافت نشد")
    return db_course


@app.put("/updatecourse/{course_id}", response_model=schemas.Course)
def update_course(course_id: str, course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.update_course(db, course_id, course)
    if db_course is None:
        raise HTTPException(status_code=404, detail= "!درس یافت نشد")
    validation.validation_course(course)
    return db_course


@app.delete("/deletecourse/{course_id}", response_model= schemas.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail= " !درس یافت نشد")
    crud.delete_course(db, course_id)
    return db_course
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

#-Student----------------------------------------------------------------------------------

@app.post("/createstudent/" , response_model = schemas.Student)
def create_student(student: schemas.Student , db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student.STID)
    if db_student:
        raise HTTPException(status_code= 400, detail= "student is already registerd")
    validation.validation_student(student)
    error = {}
    scourseids = student.SCourseIDs.split(",")
    for i in scourseids:
        db_relation_scourse = crud.get_course(db , i)
        if db_relation_scourse is None:
            error["SCourseID"]= '!درس انتخاب شده جزو دروس ارایه شده این ترم نمی باشد'
    lids = student.LIds.split(",")
    for i in lids:
        db_relation_lids = crud.get_professor(db , i)
        if db_relation_lids == None:
            error["LIDs"]= '!استاد انتتخاب شده این ترم درسی را ارایه نمی کند'
    if error:
        raise HTTPException(status_code= 400 , detail= error)
    return crud.create_student(db, student)


@app.get("/getstudent/{student_id}" , response_model= schemas.Student)
def read_student(student_id: int , db: Session= Depends(get_db)):
    db_student= crud.get_student(db , student_id)
    if db_student is None:
        raise HTTPException(status_code= 404 , detail= "Student not found!")
    return db_student


@app.put("/updatestudent/{student_id}", response_model= schemas.Student)
def update_student(student_id: str, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail= "Student not found")
    validation.validation_student(student)
    error = {}
    scourseids = student.SCourseIDs.split(",")
    for i in scourseids:
        db_relation_scourse = crud.get_course(db , i)
        if db_relation_scourse is None:
            error["SCourseID"]= '!درس انتخاب شده جزو دروس ارایه شده این ترم نمی باشد'
    lids = student.LIds.split(",")
    for i in lids:
        db_relation_lids = crud.get_professor(db , i)
        if db_relation_lids == None:
            error["LIDs"]= '!استاد انتتخاب شده این ترم درسی را ارایه نمی کند'
    if error:
        raise HTTPException(status_code= 400 , detail= error)
    return db_student

 
@app.delete("/deletestudent/{student_id}", response_model= schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code= 404, detail= "student not found")
    crud.delete_student(db , student_id)
    return db_student
    


#-professor--------------------------------------------------------------------------


@app.post("/createprofessor/", response_model= schemas.Professor)
def create_professor(professor: schemas.Professor, db: Session = Depends(get_db)):
    
    db_professor = crud.get_professor(db, professor.LID)
    if db_professor:
        raise HTTPException(status_code= 400, detail= "Professor is already registerd")
    validation.validation_professor(professor)
    error = {}
    lcourseid = professor.LCourseIDs.split(",")
    for i in lcourseid:
        db_relation_lcourse = crud.get_course(db , i)
        if db_relation_lcourse == None:
            error["LCouurseIDs"]= '!کد درس انتخاب شدخ جز دروس این ترم نمی باشد'
    if error:
        raise HTTPException(status_code= 400 , detail= error)
    return crud.create_professor(db= db, professor= professor)


@app.get("/getprofessor/{professor_id}", response_model= schemas.Professor)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "Professor not found!")
    return db_professor



@app.put("/professor/{professor_id}", response_model= schemas.Professor)
def update_professor(professor_id: str, professor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = crud.update_professor(db, professor_id, professor)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "Professor not found!")
    validation.validation_professor(professor)
    error = {}
    lcourseid = professor.LCourseIDs.split(",")
    for i in lcourseid:
        db_relation_lcourse = crud.get_course(db , i)
        if db_relation_lcourse == None:
            error["LCouurseIDs"]= '!کد درس انتخاب شدخ جز دروس این ترم نمی باشد'
    if error:
        raise HTTPException(status_code= 400 , detail= error)
    return db_professor



@app.delete("/deleteprofessor/{professor_id}", response_model= schemas.Professor)
def delete_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "Professor not found!")
    crud.delete_professor(db , professor_id)
    return db_professor


#-course-----------------------------------------------------------------------
@app.post("/CreateCourse/", response_model = schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    validation.validation_course(course)
    db_course = crud.get_course(db, course_id = course.CID)
    if db_course:
        raise HTTPException(status_code=400, detail="Course is already exists")
    return crud.create_course(db=db, course=course)


@app.get("/getCourse/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id= course_id)
    if db_course is None:
        raise HTTPException(status_code= 404, detail= "Course not found")
    return db_course


@app.put("/updatecourse/{course_id}", response_model=schemas.Course)
def update_course(course_id: str, course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.update_course(db, course_id, course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    validation.validation_course(course)
    return db_course


@app.delete("/deletecourse/{course_id}", response_model= schemas.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail= "Course not found")
    crud.delete_course(db, course_id)
    return db_course
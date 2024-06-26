from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import schemas
from sql_app import crud, models
from sql_app.database import SessionLocal, engine



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

@app.post("/createSudent/" , response_model = schemas.Student)
def create_student(student: schemas.Student , db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id= student.STID)
    if db_student:
        raise HTTPException(status_code= 400, detail= "student is already registerd")
    return crud.create_student(db= db, student= student)


@app.get("/getstudent/{student_id}" , response_model= schemas.Student)
def read_student(student_id: int , db: Session= Depends(get_db)):
    db_student= crud.get_student(db , student_id= student_id)
    if db_student is None:
        raise HTTPException(status_code= 404 , detail= "Student not found!")
    return db_student


@app.put("/updatestudent/{student_id}", response_model= schemas.Student)
def update_student(student_id: str, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail= "Student not found")
    return db_student

 
@app.delete("/deletestudent/{student_id}", response_model= schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id= student_id)
    if db_student is None:
        raise HTTPException(status_code= 404, detail= "student not found")
    crud.delete_student(db , Student_id= student_id)
    return db_student


#-professor--------------------------------------------------------------------------


@app.post("/createprofessor/", response_model= schemas.Professor)
def create_professor(professor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id= professor.LID)
    if db_professor:
        raise HTTPException(status_code= 400, detail= "Professor is already registerd")
    return crud.create_professoe(db= db, professor= professor)


@app.get("/getprofessor/{professor_id}", response_model= schemas.Professor)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id= professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "Professor not found!")
    return db_professor



@app.put("/professor/{professor_id}", response_model= schemas.Professor)
def update_professor(professor_id: str, prefessor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = crud.update_prefessor(db, professor_id, prefessor)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "Professor not found!")
    return db_professor



@app.delete("/deleteprofessor/{professor_id}", response_model= schemas.Professor)
def delete_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id=professor_id)
    if db_professor is None:
        raise HTTPException(status_code= 404, detail= "Professor not found!")
    crud.delete_professor(db , Professor_id= professor_id)
    return db_professor


#-course-----------------------------------------------------------------------
@app.post("/CreateCourse/", response_model = schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id = course.Cid)
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
    return db_course


@app.delete("/deletecourse/{course_id}", response_model=schemas.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.delete_course(db, Course_id = course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    crud.delete_course(db, id= course_id)
    return f"course with {course_id} id was deleted succesfully!"
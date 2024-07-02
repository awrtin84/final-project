from sqlalchemy.orm import Session
import schemas
from DB import models

#-Student-------------------------------------------------------------------------------------------------------------------------------------

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.STID == student_id).first()


def create_student(db: Session , student: schemas.Student):
    db_student = models.Student(STID = student.STID, FName = student.FName , LName = student.LName , Father = student.Father , Birth = student.Birth , IDS = student.IDS ,BornCity = student.BornCity,Address = student.Address , PostalCode = student.PostalCode , CPhone = student.CPhone , HPhone = student.HPhone , Department = student.Department , Major = student.Major , Married = student.Married , ID = student.ID , SCourseIDs = student.SCourseIDs ,LIds = student.LIds )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student



def update_student(db: Session , student_id: int , student = models.Student):
    db_student = db.query(models.Student).filter(models.Student.STID == student_id).first()
    if db_student is None:
        return db_student
    else:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
        return db_student



def delete_student(db: Session , student_id: int):
    db_student = db.query(models.Student).filter(models.Student.STID == student_id).first()
    db.delete(db_student)
    db.commit()

#-professor------------------------------------------------------------------------------------------------------------------------------------------


def get_professor(db: Session , professor_id: int):
    return db.query(models.Professor).filter(models.Professor.LID == professor_id).first()


def create_professor(db: Session , professor: schemas.Professor):
    db_professor  = models.Professor(LID = professor.LID , Fname = professor.Fname , Lname = professor.Lname , ID = professor.ID , Department = professor.Department ,Major = professor.Major , Birth = professor.Birth , BornCity = professor.BornCity , Address = professor.Address ,  PostalCode = professor.PostalCode ,CPhone = professor.CPhone , Hphone = professor.Hphone , LCourseIDs = professor.LCourseIDs)
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor



def update_professor(db: Session , professor_id: int , professor: models.Professor):
    db_professor = db.query(models.Professor).filter(models.Professor.LID == professor_id).first()
    if db_professor is None:
        return db_professor
    else: 
        for key, value in professor.dict().items():
            setattr(db_professor , key , value)
        db.commit()
        db.refresh(db_professor)
        return db_professor
    


def delete_professor(db: Session , professor_id: int):
    db_professor = db.query(models.Professor).filter(models.Professor.LID == professor_id).first()
    db.delete(db_professor)
    db.commit()

#Course------------------------------------------------------------------------------------------------------------------------------------

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.CID == course_id).first()


def create_course(db: Session, course: schemas.Course):
    db_course = models.Course(CID = course.Cid ,CName = course.CName , Department = course.Department , Credit = course.Credit  )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.CID == course_id).first()
    if db_course is None:
        return None
    else:
        for key, value in course.dict().items():
            setattr(db_course , key , value)
        db.commit()
        db.refresh(db_course)
        return db_course
    


def delete_course(db: Session , course_id: int):
    db_course = db.query(models.Course).filter(models.Course.CID == course_id).first()
    db.delete(db_course)
    return db_course    
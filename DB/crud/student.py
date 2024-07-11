from sqlalchemy.orm import Session
from Schemas import student as schemas
from Models import student as models



def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.STID == student_id).first()


def create_student(db: Session , student: schemas.Student):
    db_student = models.Student(STID = student.STID, FirstName = student.FirstName , LastName = student.LastName , FatherName = student.FatherName , DateOfBirth = student.DateOfBirth , IDS = student.IDS ,BornCity = student.BornCity,Address = student.Address , PostalCode = student.PostalCode , CellPhone = student.CellPhone , HomePhone = student.HomePhone , Department = student.Department , Major = student.Major , Married = student.Married , ID = student.ID , SCourseIDs = student.SCourseIDs ,LIDs = student.LIDs )
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
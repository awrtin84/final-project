from sqlalchemy.orm import Session
from Schemas import course as schemas
from Models import course as models



def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.CID == course_id).first()


def create_course(db: Session, course: schemas.Course):
    db_course = models.Course(CID = course.CID ,CourseName = course.CourseName , Department = course.Department , Credit = course.Credit  )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



def update_course(db: Session, course_id: int, course: schemas.Course):
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
    db.commit()    
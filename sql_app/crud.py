from sqlalchemy.orm import Session
from . import models, schemas


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.cid == course_id).first()

def create_course(db: Session, course: schemas.Course):
    db_course = models.Course(CID = course.cid ,CName = course.cname , Department = course.department , Credit = course.credit  )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.CID == course_id).first()
    if db_course is None:
        return None
    for key, value in course
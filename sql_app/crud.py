from sqlalchemy.orm import Session
from . import models, schemas


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.cid == course_id).first()

def create_course(db: Session, course: schemas.Course):
    db_course = models.Course(cid = course.cid ,cname = course.cname , department = course.department , credit = course.credit  )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
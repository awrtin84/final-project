from sqlalchemy.orm import Session
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from . import models, schem


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.cid == course_id).first()

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

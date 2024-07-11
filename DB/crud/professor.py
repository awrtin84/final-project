from sqlalchemy.orm import Session
from Schemas import professor as schemas
from Models import professor as models


def get_professor(db: Session , professor_id: int):
    return db.query(models.Professor).filter(models.Professor.LID == professor_id).first()


def create_professor(db: Session , professor: schemas.Professor):
    db_professor  = models.Professor(LID = professor.LID , FirstName = professor.FirstName , LastName = professor.LastName , ID = professor.ID , Department = professor.Department ,Major = professor.Major , DateOfBirth = professor.DateOfBirth , BornCity = professor.BornCity , Address = professor.Address ,  PostalCode = professor.PostalCode ,CellPhone = professor.CellPhone , HomePhone = professor.HomePhone , LCourseIDs = professor.LCourseIDs)
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

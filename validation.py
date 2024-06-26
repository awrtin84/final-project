from fastapi import HTTPException

class valdation_stu:
    "This is a class for student table validating"

    def validate_STID(STID):
        if len(int(STID)) != 11:
            raise HTTPException(status_code = 400 , detail = "Student nuhmber must be less than 11 digits!")
         

    def validate_name(FName,LName,Father):
        try:
            if not len(FName,LName,Father) <10:
                raise HTTPException(status_code= 404 , detail="Names must be less than 10 words!")
        finally:
            pass
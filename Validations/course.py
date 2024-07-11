import re
from fastapi import HTTPException


def validation_course(course):

    errors = {}

    name_pattern = r"[آ-ی\s]+"
    if re.fullmatch(pattern= name_pattern , string= course.CourseName) == None or len(course.CourseName) > 25:
        errors["CourseName"]= '!نام درس باید فارسی و کمتر از 25 کارکتر باشد'
    
    cid_pattern = r"\d{5}"
    if re.fullmatch(pattern= cid_pattern , string= course.CID) == None:
        errors["CID"]= '!کد درس باید عددی 5 رقمی باشد'

    department_pattern = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    if re.fullmatch(pattern= department_pattern , string= course.Department) == None:
        errors["Department"]= '!دانشکده باید از دانشکده های مجاز باشد'
    
    if not 1 <= course.Credit <= 4:
        errors["Credit"]= '!واحد دروس باید عددی بین 1 تا 4 باشد'

    if errors:
        raise HTTPException(status_code= 400 , detail= errors)
import re
from fastapi import HTTPException


def validation_professor(professor):


    errors= {}

    if len(str(professor.LID)) != 6 :
        errors["LID"]= '!کد استاد باید عددی 6 رقمی باشد'

    names_pattern = r"[آ-ی\s]+"
    if re.fullmatch(pattern= names_pattern , string= professor.FirstName) == None or len(professor.FirstName) > 10:
        errors["FirstName"]= '!نام باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= professor.LastName) == None or len(professor.LastName) > 10:
        errors["LastName"]= '!نام خانوادگی باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    id_pattern = r"^[1-9]\d{9}$"
    def check_professor_id(ID):
        sum = 0 
        l = 10
        for i in range(0 , l - 1):
            c = ord(ID[i])
            c -= 48
            sum = sum + c * (l - i)
        r = sum % 11
        c = ord(ID[l - 1])
        c -= 48
        if r > 2:
            r = 11 - r
        if r == c:
            return True
        else:
            return False
        
    if re.fullmatch(pattern= id_pattern , string= professor.ID) == None or check_professor_id(professor.ID) == False:
        errors["ID"]= '!شماره ملی نامعتبر می باشد'

    department_pattern = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    if re.fullmatch(pattern= department_pattern , string= professor.Department) == None:
        errors["Department"]= '!دانشکده باید یکی از دانشکده های مجاز باشد'

    major_pattern = r"(مهندسی کامپیوتر|مهندسی نفت|مهندسی برق|مهندسی پلیمر|مهندسی مکانیک|مهندسی پزشکی|مهندسی عمران|مهندسی معماری|مهندسی معدن|شهرسازی|)"
    if re.fullmatch(pattern= major_pattern , string= professor.Major) == None:
        errors["Major"]= '!رشته تحصیلی باید یکی از رشته های دانشکده فنی و مهندسی باشد '   

    birth_pattern = r"^(\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01]))"
    if re.fullmatch(pattern=birth_pattern , string= professor.DateOfBirth) == None:
        errors["Birth"]= '!تاریخ تولد وارد شده نامعتبر می باشد'

    borncity_pattern = r"(اردبیل|ارومیه|اصفهان|ایلام|تبریز|تهران|کرج|بوشهر|بیرجند|شهرکرد|مشهد|اهواز|بجنورد|زهدان|سمنان|زنجان|قم|قزوین|شیراز|ساری|سنندج|کرمان|کرمانشاه|یاسوج|گرگان|خرم آباد|رشت|اراک|بندرعباس|یزد|همدان)"
    if re.fullmatch(pattern= borncity_pattern , string= professor.BornCity) == None:
        errors["BornCity"]= '!شهر محل تولد باید یکی از مراکز استانها باشد '

    if len(professor.Address) > 100:
        errors["Address"]= '!آدرس محل زندگی باید کمتر از 100 کارکتر باشد'

    if len(str(professor.PostalCode)) != 10:
        errors["PostalCode"]= '!کد پستی باید عددی 10 رقم باشد'

    cphone_pattern = r"^(09|\+989)(\d{9})$"
    if re.fullmatch(pattern= cphone_pattern , string= professor.CellPhone) == None:
        errors["CellPhone"]= '!شماره تلفن همراه نامعتبر می باشد'

    hphone_pattern = r"^(0[1-9][0-9])([1-9]\d{7})$"
    if re.fullmatch(pattern= hphone_pattern , string= professor.HomePhone) == None:
        errors["HomePhone"]= ' !شماره تلفن ثابت نامعتبر می باشد'

    lcourseid = professor.LCourseIDs.split(",")
    for i in lcourseid:
        if len(i) != 5 or i.isdigit() == False:
            errors["LCourseIDs"]=f'باید عددی 5 رقمی باشد {i} !و به وسیله کاما از  باقی جدا شود'

    if errors:        
        raise HTTPException(status_code= 400 , detail= errors)

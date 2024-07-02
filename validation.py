import re
from fastapi import HTTPException



def validation_student(student):
    names_pattern = r"[آ-ی\s]+"
    stid_pattern = r"^(([400-402])114150([01-99]))"
    birth_pattern = r"^(\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01]))"
    ids_pattern = r"^([1-9][0-9]{5})\/([آ-ی])([01-99])$"
    borncity_pattern = r"(اردبیل|ارومیه|اصفهان|ایلام|تبریز|تهران|کرج|بوشهر|بیرجند|شهرکرد|مشهد|اهواز|بجنورد|زهدان|سمنان|زنجان|قم|قزوین|شیراز|ساری|سنندج|کرمان|کرمانشاه|یاسوج|گرگان|خرم آباد|رشت|اراک|بندرعباس|یزد|همدان)"
    cphone_pattern = r"^(09|\+989)(\d{9})$"
    hphone_pattern = r"^(0[1-9][0-9])([1-9]\d{7})$"
    department_pattern = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    major_pattern = r"(مهندسی کامپیوتر|مهندسی نفت|مهندسی برق|مهندسی پلیمر|مهندسی مکانیک|مهندسی پزشکی|مهندسی عمران|مهندسی معماری|مهندسی معدن|شهرسازی|)"
    married_pattern = r"(متاهل|مجرد)"
    id_pattern = r"^[1-9]\d{9}$"


    errors = {}
    if re.fullmatch(pattern= names_pattern , string= student.FName) == None or len(student.FName) > 10:
        errors["name"]= '!نام باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= student.LName) == None or len(student.LName) > 10:
        errors["Fname"]= '!نام خانوادگی باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= student.DName) == None or len(student.DName) > 10:
        errors["Dname"]= '!نام پدر باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '
        
    if re.fullmatch(pattern= stid_pattern , string= student.STID) == None or len(student.STID) > 11:
        errors["STID"]= '!شماره دانشجویی را با فرمت درست وارد نمایید '

    if re.fullmatch(pattern=birth_pattern , string= student.Birth) == None:
        errors["Birth"]= '!تاریخ تولد وارد شده نامعتبر می باشد'

    if re.fullmatch(pattern=ids_pattern , string= student.IDS) == None:
        errors["IDS"]= '!سریال شناسنامه نامعتبر می باشد'

    if re.fullmatch(pattern= borncity_pattern , string= student.BornCity) == None:
        errors["BornCity"]= '!شهر محل تولد باید یکی از مراکز استانها باشد '
    
    if len(student.Address) > 100:
        errors["Address"]= '!آدرس محل زندگی باید کمتر از 100 کارکتر باشد'

    if len(student.PostalCode) != 10 or student.PostalCode.isdigit() == None:
        errors["PostalCode"]= '!کد پستی باید عددی 10 رقم باشد'

    if re.fullmatch(pattern= cphone_pattern , string= student.CPhone) == None:
        errors["CPhone"]= '!شماره تلفن همراه نامعتبر می باشد'
    
    if re.fullmatch(pattern= hphone_pattern , string= student.HPhone) == None:
        errors["HPhone"]= ' !شماره تلفن ثابت نامعتبر می باشد'

    if re.fullmatch(pattern= department_pattern , string= student.Department) == None:
        errors["Department"]= '!دانشکده باید یکی از دانشکده های مجاز باشد'

    if re.fullmatch(pattern= major_pattern , string= student.Major) == None:
        errors["Major"]= '!رشته تحصیلی باید یکی از رشته های دانشکده فنی و مهندسی باشد '

    if re.fullmatch(pattern= married_pattern , string= student.Married) == None:
        errors["Married"]= '!وضعیت تاهل باید با متاهل یا مجرد تکمیل گردد '
        
    if re.fullmatch(pattern= id_pattern , string= student.ID) == None:
        errors["ID"]= '!شماره ملی نامعتبر می باشد'
    
    if errors:
        raise HTTPException(status_code= 400 , detail= errors)



def validation_professor(professor):
    lid_pattern = r"\d{6}"
    names_pattern = r"[آ-ی\s]+"
    id_pattern = r"^[1-9]\d{9}$"
    department_pattern = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    major_pattern = r"(مهندسی کامپیوتر|مهندسی نفت|مهندسی برق|مهندسی پلیمر|مهندسی مکانیک|مهندسی پزشکی|مهندسی عمران|مهندسی معماری|مهندسی معدن|شهرسازی|)"
    birth_pattern = r"^(\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01]))"
    borncity_pattern = r"(اردبیل|ارومیه|اصفهان|ایلام|تبریز|تهران|کرج|بوشهر|بیرجند|شهرکرد|مشهد|اهواز|بجنورد|زهدان|سمنان|زنجان|قم|قزوین|شیراز|ساری|سنندج|کرمان|کرمانشاه|یاسوج|گرگان|خرم آباد|رشت|اراک|بندرعباس|یزد|همدان)"
    cphone_pattern = r"^(09|\+989)(\d{9})$"
    hphone_pattern = r"^(0[1-9][0-9])([1-9]\d{7})$"


    errors= {}

    if re.fullmatch(pattern=lid_pattern , string= professor.LID) == None:
        errors["LID"]= '!کد استاد باید عددی 6 رقمی باشد می باشد'

    if re.fullmatch(pattern= names_pattern , string= professor.FName) == None or len(professor.FName) > 10:
        errors["Name"]= '!نام باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= professor.LName) == None or len(professor.LName) > 10:
        errors["FName"]= '!نام خانوادگی باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= id_pattern , string= professor.ID) == None:
        errors["ID"]= '!شماره ملی نامعتبر می باشد'

    if re.fullmatch(pattern= department_pattern , string= professor.Department) == None:
        errors["Department"]= '!دانشکده باید یکی از دانشکده های مجاز باشد'

    if re.fullmatch(pattern= major_pattern , string= professor.Major) == None:
        errors["Major"]= '!رشته تحصیلی باید یکی از رشته های دانشکده فنی و مهندسی باشد '   

    if re.fullmatch(pattern=birth_pattern , string= professor.Birth) == None:
        errors["Birth"]= '!تاریخ تولد وارد شده نامعتبر می باشد'

    if re.fullmatch(pattern= borncity_pattern , string= professor.BornCity) == None:
        errors["BornCity"]= '!شهر محل تولد باید یکی از مراکز استانها باشد '

    if len(professor.Address) > 100:
        errors["Address"]= '!آدرس محل زندگی باید کمتر از 100 کارکتر باشد'

    if len(professor.PostalCode) != 10 or professor.PostalCode.isdigit() == None:
        errors["PostalCode"]= '!کد پستی باید عددی 10 رقم باشد'

    if re.fullmatch(pattern= cphone_pattern , string= professor.CPhone) == None:
        errors["CPhone"]= '!شماره تلفن همراه نامعتبر می باشد'
    
    if re.fullmatch(pattern= hphone_pattern , string= professor.HPhone) == None:
        errors["HPhone"]= ' !شماره تلفن ثابت نامعتبر می باشد'

    if errors:
        raise HTTPException(status_code= 400 , detail= errors)



def validation_course(course):
    name_pattern = r"[آ-ی\s]+"
    cid_pattern = r"\d{5}"
    department_pattern = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    credits_pattern = r"[1-4]"


    errors = {}
    if re.fullmatch(pattern= name_pattern , string= course.CName) == None or len(course.CName) > 25:
        errors["CName"]= '!نام درس باید فارسی و کمتر از 25 کارکتر باشد'
    
    if re.fullmatch(pattern= cid_pattern , string= course.CID) == None:
        errors["CID"]= '!کد درس باید عددی 5 رقمی باشد'

    if re.fullmatch(pattern= department_pattern , string= course.Department) == None:
        errors["Department"]= '!دانشکده باید از دانشکده های مجاز باشد'
    
    if re.fullmatch(pattern= credits_pattern , string= course.Credit) == None:
        errors["Credit"]= '!تعداد واحد باید بین 1 تا 4 باشد'

    if errors:
        raise HTTPException(status_code= 400 , detail= errors)
import re
from fastapi import HTTPException


def validation_student(student):

    errors = {}


    names_pattern = r"[آ-ی\s]+"
    if re.fullmatch(pattern= names_pattern , string= student.FirstName) == None or len(student.FirstName) > 10:
        errors["FirstName"]= '!نام باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= student.LastName) == None or len(student.LastName) > 10:
        errors["Lastname"]= '!نام خانوادگی باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= student.FatherName) == None or len(student.FatherName) > 10:
        errors["FatherName"]= '!نام پدر باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '
        
    stid_pattern = r"^(400|401|402|403)114150([01-99]{2})$"
    if re.fullmatch(pattern= stid_pattern , string= student.STID) == None or len(student.STID) != 11:
        errors["STID"]= '!شماره دانشجویی را با فرمت درست وارد نمایید '

    birth_pattern = r"^(\d{4}\/(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01]))"
    if re.fullmatch(pattern=birth_pattern , string= student.DateOfBirth) == None:
        errors["Birth"]= '!تاریخ تولد وارد شده نامعتبر می باشد'

    ids_pattern = r"([0-9]{6})\/([آ-ی])[0-9]{2}"
    if re.fullmatch(pattern=ids_pattern , string= student.IDS) == None:
        errors["IDS"]= '!سریال شناسنامه نامعتبر می باشد'

    borncity_pattern = r"(اردبیل|ارومیه|اصفهان|ایلام|تبریز|تهران|کرج|بوشهر|بیرجند|شهرکرد|مشهد|اهواز|بجنورد|زهدان|سمنان|زنجان|قم|قزوین|شیراز|ساری|سنندج|کرمان|کرمانشاه|یاسوج|گرگان|خرم آباد|رشت|اراک|بندرعباس|یزد|همدان)"
    if re.fullmatch(pattern= borncity_pattern , string= student.BornCity) == None:
        errors["BornCity"]= '!شهر محل تولد باید یکی از مراکز استانها باشد '
    
    if len(student.Address) > 100:
        errors["Address"]= '!آدرس محل زندگی باید کمتر از 100 کارکتر باشد'

    if len(str(student.PostalCode)) != 10:
        errors["PostalCode"]= '!کد پستی باید عددی 10 رقم باشد'

    cphone_pattern = r"^(09|\+989)(\d{9})$"
    if re.fullmatch(pattern= cphone_pattern , string= student.CellPhone) == None:
        errors["CellPhone"]= '!شماره تلفن همراه نامعتبر می باشد'
    
    hphone_pattern = r"^(0[1-9][0-9])([1-9]\d{7})$"
    if re.fullmatch(pattern= hphone_pattern , string= student.HomePhone) == None:
        errors["HomePhone"]= ' !شماره تلفن ثابت نامعتبر می باشد'

    department_pattern = r"(فنی و مهندسی|اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    if re.fullmatch(pattern= department_pattern , string= student.Department) == None:
        errors["Department"]= '!دانشکده باید یکی از دانشکده های مجاز باشد'

    major_pattern = r"(مهندسی کامپیوتر|مهندسی نفت|مهندسی برق|مهندسی پلیمر|مهندسی مکانیک|مهندسی پزشکی|مهندسی عمران|مهندسی معماری|مهندسی معدن|شهرسازی|)"
    if re.fullmatch(pattern= major_pattern , string= student.Major) == None:
        errors["Major"]= '!رشته تحصیلی باید یکی از رشته های دانشکده فنی و مهندسی باشد '

    married_pattern = r"(متاهل|مجرد)"
    if re.fullmatch(pattern= married_pattern , string= student.Married) == None:
        errors["Married"]= '!وضعیت تاهل باید با متاهل یا مجرد تکمیل گردد '
        
    id_pattern = r"^[1-9]\d{9}$"

    def check_student_id(ID):
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
        
    if re.fullmatch(pattern= id_pattern , string= student.ID) == None or check_student_id(student.ID) == False:
        errors["ID"]= '!کد ملی نامعتبر می باشد'

    scourseids = student.SCourseIDs.split(",")
    for i in scourseids:
        if len(i) != 5 or i.isdigit() == False:
            errors["SCourseIDs"]= f'باید عددی 5 رقمی باشد {i} !و به وسیله کاما از  باقی جدا شود' 

        lids = student.LIDs.split(",")
    for i in lids:
        if len(i) != 6 or i.isdigit() == False:
            errors["LIDs"]= f'باید عددی 6 رقمی باشد {i} !و به وسیله کاما از  باقی جدا شود'


    if errors:
        raise HTTPException(status_code= 400 , detail= errors)

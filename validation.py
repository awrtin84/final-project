import re


def validation_student(Student):
    names_pattern = r"[آ-ی\s]+"
    stid_pattern = r"^([400-402])114150([01-99])$"
    birth_pattern = r"^([1300-1384])/(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])$"
    ids_pattern = r"^([1-9][0-9]{5})/([آ-ی])([01-99])$"
    borncity_pattern = r"(اردبیل|ارومیه|اصفهان|ایلام|تبریز|تهران|کرج|بوشهر|بیرجند|شهرکرد|مشهد|اهواز|بجنورد|زهدان|سمنان|زنجان|قم|قزوین|شیراز|ساری|سنندج|کرمان|کرمانشاه|یاسوج|گرگان|خرم آباد|رشت|اراک|بندرعباس|یزد|همدان)"
    cphone_pattern = r"^(09|\+989)(\d{9})$"
    hphone_pattern = r"^(0[1-9][0-9])([1-9]\d{7})$"
    department_pattern = r"(فنی و مهندسی |اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    major_pattern = r"(مهندسی کامپیوتر|مهندسی نفت|مهندسی برق|مهندسی پلیمر|مهندسی مکانیک|مهندسی پزشکی|مهندسی عمران|مهندسی معماری|مهندسی معدن|شهرسازی|)"
    married_pattern = r"(متاهل|مجرد)"
    id_pattern = r"^[1-9]\d{9}$"

    errors = {}
    if re.fullmatch(pattern= names_pattern , string= Student.FName) == None or len(Student.FName) > 10:
        errors["name"]= '!نام باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= Student.LName) == None or len(Student.LName) > 10:
        errors["Fname"]= '!نام خانوادگی باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '

    if re.fullmatch(pattern= names_pattern , string= Student.DName) == None or len(Student.DName) > 10:
        errors["Dname"]= '!نام پدر باید فقط با حروف فارسی و کمتر از 10 کارکتر باشند '
        
    if re.fullmatch(pattern= stid_pattern , string= Student.STID) == None or len(Student.STID) > 11:
        errors["STID"]= '!شماره دانشجویی را با فرمت درست وارد نمایید '

    if re.fullmatch(pattern=birth_pattern , string= Student.Birth) == None:
        errors["Birth"]= '!تاریخ تولد وارد شده نامعتبر می باشد'

    if re.fullmatch(pattern=ids_pattern , string= Student.IDS) == None:
        errors["IDS"]= '!سریال شناسنامه نامعتبر می باشد'

    if re.fullmatch(pattern= borncity_pattern , string= Student.BornCity) == None:
        errors["BornCity"]= '!شهر محل تولد باید یکی از مراکز استانها باشد '
    
    if len(Student.Address) > 100:
        errors["Address"]= '!آدرس محل زندگی باید کمتر از 100 کارکتر باشد'

    if len(Student.PostalCode) > 10 or Student.PostalCode.isdigit() == None:
        errors["PostalCode"]= '!کد پستی باید عددی 10 رقم باشد'

    if re.fullmatch(pattern= cphone_pattern , string= Student.CPhone) == None:
        errors["CPhone"]= '!شماره تلفن همراه نامعتبر می باشد'
    
    if re.fullmatch(pattern= hphone_pattern , string= Student.HPhone) == None:
        errors["HPhone"]= ' !شماره تلفن ثابت نامعتبر می باشد'

    if re.fullmatch(pattern= department_pattern , string= Student.Department) == None:
        errors["Department"]= '!دانشکده باید یکی از دانشکده های مجاز باشد'

    if re.fullmatch(pattern= major_pattern , string= Student.Major) == None:
        errors["Major"]= '!رشته تحصیلی باید یکی از رشته های مجاز باشد '

    if re.fullmatch(pattern= married_pattern , string= Student.Married) == None:
        errors["Married"]= '!وضعیت تاهل باید با متاهل یا مجرد تکمیل گردد '
        
    if re.fullmatch(pattern= id_pattern , string= Student.ID) == None:
        errors["ID"]= '!شماره ملی نامعتبر می باشد'
    



def validation_course(Course):
    name_pattern = r"[آ-ی\s]+"
    cid_pattern = r"\d{5}"
    department_pattern = r"(فنی و مهندسی |اقتصاد|علوم پایه|ادبیات|منابع طبیعی|کشاورزی)"
    credits_pattern = r"[1-4]"


    errors = {}
    if re.fullmatch(pattern= name_pattern , string= Course.CName) == None or len(Course.CName) > 25:
        errors["CName"]= '!نام درس باید فارسی و کمتر از 25 کارکتر باشد'
    
    if re.fullmatch(pattern= cid_pattern , string= Course.CID) == None:
        errors["CID"]= '!کد درس باید عددی 5 رقمی باشد'

    if re.fullmatch(pattern= department_pattern , string= Course.Department) == None:
        errors["Department"]= '!دانشکده باید از دانشکده های مجاز باشد'
    
    if re.fullmatch(pattern= credits_pattern , string= Course.Credit) == None:
        errors["Credit"]
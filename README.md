# بسم االله الرحمن الرحیم
## گزارش کار پروژه:
## این پروژه یک برنامه تحت وب است که با استفاده از فریمورک FastAPI پیاده‌سازی شده است. این برنامه شامل مدیریت اطلاعات دانشجویان، اساتید و دوره‌ها است و از SQLAlchemy برای مدیریت پایگاه داده استفاده می‌کند.
### ساختار پروژه:

پروژه شامل فایل‌ها و پوشه‌های زیر است:

1. فایل‌های اصلی:
   - __init__.py
   - config.py
   - depends.py
   - main.py
   - validation.py

2. پوشه DB:
   - __init__.py
   - database.py
   - پوشه crud:
      - __init__.py
      - course.py
      - professor.py
      - student.py

3. پوشه models:
   - __init__.py
   - course.py
   - professor.py
   - student.py

4. پوشه routers:
   - __init__.py
   - course.py
   - professor.py
   - student.py

5. پوشه schemas:
   - __init__.py
   - course.py
   - professor.py
   - student.py

     
## فایل main.py:
این فایل برنامه را با استفاده از uvicorn اجرا می‌کند:
![image](https://github.com/awrtin84/final-project/assets/161155080/dce1a7cb-a9ec-4aa7-8b3b-d96a685b447d)

ابن کد باعث می‌شود که برنامه با استفاده از پیکربندی موجود در فایل config.py روی پورت 8000 اجرا شود.


## فایل config.py:
این فایل شامل تنظیمات اصلی برنامه است:
![image](https://github.com/awrtin84/final-project/assets/161155080/7d767e0a-fc33-4a1d-bc30-2cbada7aa128)

- Base.metadata.create_all(bind=engine): جداول پایگاه داده را ایجاد می‌کند.
- app.include_router(...): روترهای مربوط به هر کدام از ماژول‌ها را به برنامه اضافه می‌کند.


## فایل‌های routers:
این فایل‌ها مسئول مدیریت مسیرهای مربوط به هر ماژول (دانشجو، استاد، دوره) هستند. به عنوان مثال، فایل course.py شامل کد زیر است:
![image](https://github.com/awrtin84/final-project/assets/161155080/2780f210-4ded-4c1f-94a7-c34bad303f9d)

![image](https://github.com/awrtin84/final-project/assets/161155080/13267ae6-4dc2-48f9-a2de-2993dc37cb5e)

که شامل 4 مسیر برای افزودن که به وسیله post و خواندن به وسیله get آپدیت کردن به وسیله put و حذف کردن رکورد ها به وسیله delete است. و هر رکورد به وسیله توابع موجود در crud با پایگاه داده تعامل برقرار می کنند.


## فایل‌های models:
این فایل‌ها شامل تعریف مدل‌های پایگاه داده هستند. به عنوان مثال، فایل course.py:
![image](https://github.com/awrtin84/final-project/assets/161155080/242518b2-5a26-4058-818e-814761b84f00)

که با استفاده از orm ها و کلاس پایتونی که ما برای هر جدول تعیین میکنیم برای ما ستون های جداول را تشکیل می دهد.


## فایل‌های schemas:
این فایل‌ها شامل طرح‌های (schemas) Pydantic برای تایید داده‌ها هستند. به عنوان مثال، فایل student.py:

![image](https://github.com/awrtin84/final-project/assets/161155080/a42e02ca-1971-4218-afa9-07ec2b24e2a8)

که با استفاده از آن میتوان شکل و شمایل داده های ورودی را کنترل کرد, و با قرار دادن orm_mode=True



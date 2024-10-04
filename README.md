# بسم الله الرحمن الرحیم
## گزارش کار پروژه:
## این پروژه یک برنامه تحت وب است که با استفاده از فریمورک FastAPI پیاده‌سازی شده است. این برنامه شامل مدیریت اطلاعات دانشجویان، اساتید و دوره‌ها است و از SQLAlchemy برای مدیریت پایگاه داده استفاده می‌کند.
### ساختار پروژه:

پروژه شامل فایل‌ها و پوشه‌های زیر است:

1. فایل‌های اصلی:
   - __init__.py
   - config.py
   - depends.py
   - main.py
   

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
  
6. پوشه - validation:

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


## فایل dependency.py:
این فایل برای تعریف وابستگی‌های مورد نیاز پروژه استفاده می‌شود.

![image](https://github.com/awrtin84/final-project/assets/161155080/89327efa-aaa6-4621-92a4-351d7148403d)

که در این فایل تابع ()get_db قرار دارد و وظیفه آن ساختن یک نشست یا Session برای تعامل با پایگاه داده و بستن آن نشست در پایان آن تعامل است.

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

که با استفاده از آن میتوان شکل و شمایل داده های ورودی را کنترل کرد. و با قرار دادن orm_mode=True اگر از response_model استفاده کنیم. لزومی به استفاده از دیکشنری نمی باشد و اگر یک instance نیز برای آن ارسال گردد مورد تایید می باشد.


## داکرایز کردن پروژه:

برای داکرایز کردن پروژه، از فایل‌های زیر استفاده می‌کنیم:



![image](https://github.com/awrtin84/final-project/assets/161155080/643840e6-8c6e-435c-9cd6-70d5445b50c3)

ن فایل شامل تنظیمات مورد نیاز برای ایجاد تصویر Docker از برنامه است. برای مدیریت محیط اجرا و استقرار برنامه استفاده می‌شود.


## فایل requirements.txt:

![image](https://github.com/awrtin84/final-project/assets/161155080/ffa9e739-8bc2-4cdf-8e9c-bae3312a185b)

شامل لیست کتابخانه‌ها و پکیج‌های پایتون مورد نیاز پروژه است که باید نصب شوند.


## فایل های validation.py:

در این ماژول ها قوانین و توابع اعتبارسنجی داده‌ها تعریف شده است. وظیفه این ماژول بررسی و تضمین صحت داده‌های ورودی است.که نمونه آن را برای course:

![image](https://github.com/awrtin84/final-project/assets/161155080/c2a68d78-5e21-4656-b5e1-62bebaca2423)


## تست از جدول درس در fastapi swagger:

### برای ساختن یک درس:
1-

![image](https://github.com/awrtin84/final-project/assets/161155080/f2c2c76b-3695-4ee4-822e-5c5b008767bc)

پاسخ سرور:

2-
![image](https://github.com/awrtin84/final-project/assets/161155080/1c077127-da65-4d55-83ad-cd1cb6041a59)


جدول پایگاه داده:
3-

![image](https://github.com/awrtin84/final-project/assets/161155080/c5bf88dd-316a-42de-904e-46e803d8b4fc)


### برای دریافت یک درس:
1-

![image](https://github.com/awrtin84/final-project/assets/161155080/b4c67d07-f024-4bca-a087-23630eb436bc)

پاسخ سرور:

2-

![image](https://github.com/awrtin84/final-project/assets/161155080/2a59e805-2e37-4ff4-b303-44b0ea53e632)


### برای آپدیت کردن یک درس:

1-

![image](https://github.com/awrtin84/final-project/assets/161155080/9f23a362-329d-4b16-8ce7-51da6b94b2e7)

پاسخ سرور:

2-

![image](https://github.com/awrtin84/final-project/assets/161155080/5a84a39c-c2f2-40cf-a30e-4506cfb6672e)


جدول پایگاه داده:

3-
![image](https://github.com/awrtin84/final-project/assets/161155080/638e8e69-3b75-45c2-b799-a1039010c269)


### برای حذف کردن درس:

1-

![image](https://github.com/awrtin84/final-project/assets/161155080/a593f6e2-6dc0-4f16-908e-604397bdf3ca)



پاسخ سرور:
2-

![image](https://github.com/awrtin84/final-project/assets/161155080/e358681d-4481-41c3-9a35-921a433a8fd9)

جدول پایگاه داده:

3-

![image](https://github.com/awrtin84/final-project/assets/161155080/0888b690-ef86-4b67-a66a-ebdbc2817181)


# پایان

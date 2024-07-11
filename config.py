from DB.database import engine, Base
from fastapi import FastAPI
from Routers import course, professor, student



app = FastAPI()
Base.metadata.create_all(bind=engine)


app.include_router(course.router, tags= ['Course'])
app.include_router(professor.router, tags= ['Professor'])
app.include_router(student.router, tags= ['Student'])
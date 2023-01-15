from fastapi import FastAPI

from database.database import Base, engine, SessionLocal
from database.create_language import create_languages
from router.about_me import about_me_crud
from router.contact import contact_crud
from router.education_company import education_company_crud
from router.skills import skills_crud
from router.feedback import feedback_crud 


Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(about_me_crud.router)
app.include_router(contact_crud.router)
app.include_router(education_company_crud.router)
app.include_router(skills_crud.router)
app.include_router(feedback_crud.router)


create_languages(SessionLocal())

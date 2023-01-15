from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import EducationCompany, Language


def get(db: Session, lang: str):
    query_response = db.query(EducationCompany).join(Language).filter(Language.name == lang).first()
    db.close()
    
    if query_response:
        return {
            "name": query_response.name,
            "start_education_date": query_response.start_education_date,
            "finish_education_date": query_response.finish_education_date,
            "logo": query_response.logo,
        }
    
    raise HTTPException(status_code=404, detail="Education company not found")
    
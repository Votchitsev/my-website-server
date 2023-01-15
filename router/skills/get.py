from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import EducationCompany, Language, Skill


def get(db: Session, lang: str, edu_id: int):
    query_response = db.query(Skill).join(EducationCompany).join(Language).\
        filter(EducationCompany.id == edu_id, Language.name == lang).all()

    if len(query_response):
        return {
            "name": query_response.name,
        }

    raise HTTPException(status_code=404, detail="Skill not found")
    
from sqlalchemy.orm import Session
from datetime import datetime

from database.models import EducationCompany, Skill
from router.get_language_id import get_language_id


def create(db: Session, data):
    language_id = get_language_id(data.language)
  
    skill = Skill(
        name = data.name,
        education_company_id = data.education_company_id,
        language_id = language_id
    )

    db.add(skill)

    db.commit()

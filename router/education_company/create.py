from sqlalchemy.orm import Session
from datetime import datetime

from database.models import EducationCompany
from router.get_language_id import get_language_id
from router.row_is_created import row_is_created


def create(db: Session, data):
    language_id = get_language_id(data.language)

    if row_is_created(db, language_id, EducationCompany):
        db.query(EducationCompany).filter(EducationCompany.language_id == language_id).update({
            "name": data.name,
            "start_education_date": datetime.strptime(data.start_education_date, '%Y-%m-%d'),
            "finish_education_date": datetime.strptime(data.finish_education_date, '%Y-%m-%d'),
            "logo": data.logo,
        })
        db.commit()
        return
    
    education_company = EducationCompany(
        name = data.name,
        start_education_date = datetime.strptime(data.start_education_date, '%Y-%m-%d'),
        finish_education_date = datetime.strptime(data.finish_education_date, '%Y-%m-%d'),
        logo = data.logo,
        language_id = language_id
    )

    db.add(education_company)

    db.commit()

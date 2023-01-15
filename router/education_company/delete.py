from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import EducationCompany


def delete(db: Session, id):
    edu = db.query(EducationCompany).filter(EducationCompany.id == id)

    if edu.first():
        edu.delete()

        db.commit()
        db.close()
        return
    
    db.close()
    raise HTTPException(status_code=404, detail="Education company not found")
    
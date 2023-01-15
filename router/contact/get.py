from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import Contact, Language


def get(db: Session, lang):
    query_response = db.query(Contact).join(Language).filter(Language.name == lang).first()
    db.close()
    
    if query_response:
        return {
            "name": query_response.name,
            "burth_date": query_response.burth_date,
            "city": query_response.city,
            "email": query_response.email,
            "phone": query_response.phone,
            "current_job": query_response.current_job,
            "is_active": query_response.is_active,
        }
    
    raise HTTPException(status_code=404, detail="Contact not found")
    
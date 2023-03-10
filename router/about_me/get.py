from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import AboutMe, Language


def get(db: Session, lang):
    query_response = db.query(AboutMe).join(Language).filter(Language.name == lang).first()
    db.close()
    
    if query_response:
        return {
        "text": query_response.text,
    }

    raise HTTPException(status_code=404, detail="Text not found")
    
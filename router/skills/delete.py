from fastapi import HTTPException
from sqlalchemy.orm import Session

from database.models import Skill


def delete(db: Session, id):
    skill = db.query(Skill).filter(Skill.id == id)

    if skill.first():
        skill.delete()

        db.commit()
        db.close()
        return
    
    db.close()
    raise HTTPException(status_code=404, detail="Skill not found")
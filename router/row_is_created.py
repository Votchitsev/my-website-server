from sqlalchemy.orm import Session


def row_is_created(db: Session, language_id, model):
    result = db.query(model).filter(model.language_id == language_id).all()

    if len(result) > 0:
        return True
    
    return False
    
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, validates

from .database import Base

class Language(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    @validates('name')
    def validate_name(self, _, name):
        if name != 'ru' or name != 'en':
            raise ValueError('Unexpected language name. Please, choose one of "en" or "ru"')
        return name


# class AboutMe(Base):
#     __table_name__ = 'about_me'

#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String)
#     language_id = Column(String, ForeignKey('language.id'))
#     is_active = Column(Boolean, default=True)

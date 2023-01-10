from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import relationship, validates

from .database import Base

class Language(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    about_me_text = relationship('AboutMe')
    contact_text = relationship('Contact')
    education_company_text = ('EducationCompany')
    skills_text = ('Skill')


class AboutMe(Base):
    __tablename__ = 'about_me'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    language_id = Column(String, ForeignKey('language.id'))
    is_active = Column(Boolean, default=True)


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    burth_date = Column(Date)
    city = Column(String)
    email = Column(String)
    phone = Column(String)
    current_job = Column(String)
    language_id = Column(Integer, ForeignKey('language.id'))
    is_active = Column(Boolean, default=True)


class EducationCompany(Base):
    __tablename__ = 'education_company'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    start_education_date = Column(Date)
    finish_education_date = Column(Date)
    logo = Column(String)
    language_id = Column(Integer, ForeignKey('language.id'))

    skills = relationship('Skill')


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    education_company_id = Column(Integer, ForeignKey('education_company.id'))
    language = Column(Integer, ForeignKey('language.id'))


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    name = Column(String)
    email = Column(String)
    message = Column(Text)
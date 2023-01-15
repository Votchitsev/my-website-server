from pydantic import BaseModel, validator, EmailStr


class TableWithLanguage(BaseModel):
    language: str

    @validator('language')
    def validate_language(cls, value):
        if value != 'ru' and value != 'en':
            raise ValueError('Unexpected language name. Please, choose one of en or ru')
        return value


class AboutMe(TableWithLanguage):
    text: str
    is_active: bool


class Contact(TableWithLanguage):
    name: str
    burth_date: str
    city: str
    email: str
    phone: str
    current_job: str
    is_active: bool


class Skill(TableWithLanguage):
    name: str
    education_company_id: int


class EducationCompany(TableWithLanguage):
    name: str
    start_education_date: str
    finish_education_date: str
    logo: str


class Feedback(BaseModel):
    date: str
    name: str
    email: EmailStr
    message: str
    
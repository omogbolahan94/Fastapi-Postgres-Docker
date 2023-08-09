import datetime as _dt
import pydantic as _pydantic


class _BaseContact(_pydantic.BaseModel):
    """
    Defines the basic attributes common to all contacts
    """
    first_name: str
    last_name: str
    email: str
    phone_number: str


class Contact(_BaseContact):
    """
    extends the _BaseContact with additional attributes
    """
    id: int
    date_created: _dt.datetime

    class Config:
        # for model validation when posting to database
        orm_mode = True
        from_attributes = True


class CreateContact(_BaseContact):
    """
    creating new contact records
    """
    pass
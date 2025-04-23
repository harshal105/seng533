from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId
from typing import List, Optional
from enum import Enum
from datetime import datetime


CONFIG = ConfigDict(
            min_anystr_length = 1,
            anystr_strip_whitespace = True,
        )


class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"

class MaritalStatusEnum(str, Enum):
    single = "Single"
    married = "Married"
    divorced = "Divorced"
    widowed = "Widowed"

class CurrencyEnum(str, Enum):
    USD = "USD"
    CAD = "CAD"

class TransactionTypeEnum(str, Enum):
    purchase = "purchase"
    refund = "refund"

class StatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"
    canceled = "canceled"

class StringDataPerson(BaseModel):
    model_config = CONFIG

    id: str
    first_name: str
    last_name: str
    age: Optional[str] = None  
    gender: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    date_of_birth: Optional[str] = None
    occupation: Optional[str] = None
    company: Optional[str] = None
    marital_status: Optional[str] = None
    nationality: Optional[str] = None
    language: Optional[str] = None
    hobby: Optional[str] = None
    last_updated: Optional[str] = None

class Transactions(BaseModel):
    model_config = CONFIG

    id: str
    person_id: str
    amount: float
    currency: str
    transaction_type: str
    status: str
    timestamp: int 

class MultiDataPerson(BaseModel):
    model_config = CONFIG

    id: str
    first_name: str
    last_name: str
    age: Optional[int] = None 
    gender: Optional[str] = None 
    phone: Optional[int] = None
    zip_code: Optional[str] = None
    date_of_birth: Optional[datetime] = None 
    language: Optional[List[str]] = [] 
    hobby: Optional[List[str]] = [] 


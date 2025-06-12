from typing import Optional, List, Dict
from enum import Enum
from pydantic import BaseModel

class TaskName(str, Enum):
    extractive_summarization = "extractive_summarization"
    abstractive_summarization = "abstractive_summarization"
    classification = "classification"
    five_ws_extraction = "five_ws_extraction"

class RequestorType(str, Enum):
    member = "member"
    provider = "provider"
    admin = "admin"
    system = "system"

class ReadingLevel(str, Enum):
    elementary = "elementary"
    middle_school = "middle_school"
    high_school = "high_school"
    college = "college"
    professional = "professional"

class DocumentType(str, Enum):
    transcription = "transcription"
    document = "document"
    report = "report"
    note = "note"

class Extraction5WsContainer(BaseModel):
    who: Optional[List[str]]
    what: Optional[List[str]]
    when: Optional[List[str]]
    where: Optional[List[str]]
    why: Optional[List[str]]
    supplemental: Optional[Dict[str, str]]

class RequestPayload(BaseModel):
    task_name: TaskName
    interaction_id: Optional[str] = None
    dcn: Optional[str] = None
    claims: Optional[List[str]] = None
    prior_auth: Optional[List[str]] = None
    citation: bool = False
    reasoning: bool = False
    guidelines: Optional[List[str]] = None
    requestor_type: Optional[RequestorType] = None
    reading_level: Optional[ReadingLevel] = None

    class Config:
        schema_extra = {
            "example": {
                "task_name": "five_ws_extraction",
                "interaction_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "dcn": "DOC123456",
                "citation": True,
                "reasoning": False,
                "requestor_type": "provider",
                "reading_level": "high_school"
            }
        }

class ResponsePayload(BaseModel):
    extraction: Extraction5WsContainer
    info: Optional[Dict[str, str]]
    role: Optional[str]
    response: Optional[str]
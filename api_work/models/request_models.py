from typing import List, Optional, Dict
from pydantic import BaseModel

class Document(BaseModel):
    document_type: str
    metadata: Dict[str, str]
    content: str
    prior_auth: Optional[List[str]] = None
    interaction_id: Optional[str] = None
    dcn: Optional[str] = None

class ClinicalRequest(BaseModel):
    task_name: str
    requestor_type: Optional[str]
    reading_level: Optional[str]
    document: Document
    guidelines: Optional[List[str]] = None
    glossary: Optional[str] = None
    citation: bool
    reasoning: bool
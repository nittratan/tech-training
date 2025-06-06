from pydantic import BaseModel

class Extraction5WsContainer(BaseModel):
    who: str
    what: str
    when: str
    where: str
    why: str

class ClinicalResponse(BaseModel):
    task_id: str
    extraction5WsContainer: Extraction5WsContainer

class HeartbeatResponse(BaseModel):
    info: str
    role: str
    response: str
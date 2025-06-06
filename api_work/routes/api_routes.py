from fastapi import APIRouter, status
from uuid import uuid4
from models.request_models import ClinicalRequest
from models.response_models import ClinicalResponse, HeartbeatResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/capabilities")
def get_capabilities():
    logger.info("Fetching model capabilities")
    return {"models": ["03-mini-openai"]}

@router.post("/heartbeat", response_model=HeartbeatResponse, status_code=status.HTTP_200_OK)
def heartbeat():
    return {
        "info": "Heartbeat OK",
        "role": "system",
        "response": "Alive"
    }

@router.post("/task", response_model=ClinicalResponse)
def process_task(payload: ClinicalRequest):
    return {
        "task_id": str(uuid4()),
        "extraction5WsContainer": {
            "who": "John Doe",
            "what": "Summary",
            "when": "2025-06-06",
            "where": "NYC",
            "why": "Medical necessity"
        }
    }

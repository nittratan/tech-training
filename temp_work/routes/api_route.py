from fastapi import APIRouter, HTTPException
from typing import Optional
from models.schemas import (
    RequestPayload,
    ResponsePayload,
    TaskName,
    Extraction5WsContainer
)
from uuid import uuid4

router = APIRouter()

@router.get("/capabilities", tags=["capabilities"])
async def get_capabilities():
    """Returns supported models and capabilities"""
    return {"models": ["03-mini-openai"], "capabilities": ["5Ws extraction"]}

@router.post("/heartbeat", tags=["health"])
async def heartbeat():
    """Health check endpoint"""
    return {"status": "alive"}

@router.post("/tokenize", tags=["processing"])
async def tokenize(payload: RequestPayload):
    """Tokenize input before LLM processing"""
    # Mock implementation
    return {"tokens": ["mock", "token", "list"], "count": 3}

@router.post("/generate", tags=["generation"])
async def generate(payload: RequestPayload):
    """Generate raw output from LLM"""
    # Mock implementation
    return {"output": "This is a mock generated response."}

@router.post("/generate_parsed", tags=["generation"], response_model=ResponsePayload)
async def generate_parsed(payload: RequestPayload):
    """Generate and parse 5Ws extraction"""
    
    # Mock data based on request parameters
    extraction = Extraction5WsContainer(
        who=["Dr. Smith", "patient"],
        what=["annual checkup", "blood test"],
        when=["2023-05-15"],
        where=["Main Street Clinic"],
        why=["routine health maintenance"],
        supplemental={"notes": "Patient showed normal results"}
    )
    
    response = ResponsePayload(
        extraction=extraction,
        info={"model": "03-mini-openai", "task": payload.task_name},
        role="assistant",
        response="Here is the extracted 5Ws information from the document."
    )
    
    if payload.citation:
        response.info["citation"] = "Source: Medical Records Database"
    
    if payload.reasoning:
        response.info["reasoning"] = "Extracted based on clinical notes format"
    
    return response
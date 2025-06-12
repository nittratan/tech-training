from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api_v1 import api_router
import uvicorn

app = FastAPI(
    title="NextGen 5Ws Extraction API",
    description="API for extracting Who, What, When, Where, Why from documents",
    version="0.1.0",
    openapi_url="/openapi.json"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "NextGen 5Ws Extraction API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0", port=8000, log_level="info")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api_routes import router
from utils.logger import setup_logger
from utils.exceptions import add_exception_handlers
import uvicorn


app = FastAPI(title="Clinical Task API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

setup_logger()
add_exception_handlers(app)



app.include_router(router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Clinical Task API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
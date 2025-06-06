from fastapi import FastAPI, Request
import logging
import uvicorn

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# FastAPI App
app = FastAPI()

@app.get("/ping")
def health_check():
    logger.info("Health check hit at /ping")
    return {"status": "alive"}


@app.get("/ping1")
async def ping(request: Request):
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent")

    logger.info(f"Request received from IP: {client_ip}, User-Agent: {user_agent}")

    return {"status": "Kishan's api alive", "client_ip": client_ip, "user_agent": user_agent}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
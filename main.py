from fastapi import FastAPI
from api.routes import router

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
app = FastAPI(
	title="Backend SafeZone",
	description="Backend with websockets",
	version="1.0.0"
)

app.include_router(router, prefix="/api")


@app.get("/")
async def root():
	return{"message": "Welcome to the safe zone backend!"}



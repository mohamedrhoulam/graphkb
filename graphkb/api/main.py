from fastapi import FastAPI
from graphkb.api.routes import router

app = FastAPI(title="Graph Knowledge Base API")
app.include_router(router)

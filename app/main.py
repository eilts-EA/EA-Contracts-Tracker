from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator
from .database import engine, AsyncSessionLocal
from .settings import settings
from .sam import fetch_sam_opportunities
import asyncio

app = FastAPI(title="SDVOSB Contract Tracker")
templates = Jinja2Templates(directory="app/templates")

Instrumentator().instrument(app).expose(app)

@app.on_event("startup")
async def startup():
    # create tables if needed (simplified)
    async with engine.begin() as conn:
        await conn.run_sync(lambda metadata: None)

    asyncio.create_task(periodic_sam())

async def periodic_sam():
    while True:
        try:
            data = await fetch_sam_opportunities()
            # noop: in full project we'd upsert into DB
        except Exception:
            pass
        await asyncio.sleep(max(60, settings.SAM_SYNC_INTERVAL_SECONDS))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/admin/sam", response_class=HTMLResponse)
async def sam_admin(request: Request):
    return templates.TemplateResponse("sam_admin.html", {"request": request})
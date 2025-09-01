from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from apscheduler.schedulers.background import BackgroundScheduler
from .services.news_service import news_service_instance
from .routers import news

app = FastAPI(
    title="News Summarizer App",
    description="A web app to fetch and summarize news articles.",
    version="1.0.0",
)

# Configure templates
templates = Jinja2Templates(directory="app/templates")

# --- Scheduler Setup ---
@app.on_event("startup")
def start_scheduler():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(news_service_instance.update_headlines_cache, 'interval', hours=24, id="update_headlines_job")
    scheduler.start()
    news_service_instance.update_headlines_cache()
    print("Scheduler started and initial headline fetch complete.")

# --- API Routers ---
app.include_router(news.router)

# --- Frontend Route ---
@app.get("/", response_class=HTMLResponse)
async def read_root_page(request: Request):
    # This endpoint will serve our main HTML page
    return templates.TemplateResponse("index.html", {"request": request})

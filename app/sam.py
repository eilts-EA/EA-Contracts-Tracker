import httpx
from .settings import settings

SAM_BASE = "https://api.sam.gov/opportunities/v1/search"

def _csv_to_list(s: str) -> list:
    return [x.strip() for x in (s or "").split(",") if x.strip()]

async def fetch_sam_opportunities():
    if not settings.SAM_API_KEY:
        return []
    params = {
        "api_key": settings.SAM_API_KEY,
        "limit": 100,
        "sort": "postedDate,desc",
        "naics": ",".join(_csv_to_list(settings.SAM_NAICS)),
        "setAside": settings.SAM_SETASIDE,
        "noticeType": settings.SAM_NOTICE_TYPES,
    }
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(SAM_BASE, params=params)
        r.raise_for_status()
        data = r.json()
        return data.get("opportunitiesData", [])
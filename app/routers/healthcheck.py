from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health Check"])
async def healthcheck():
    return {"status": "ok"}
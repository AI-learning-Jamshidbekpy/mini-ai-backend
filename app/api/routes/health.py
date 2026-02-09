from fastapi import APIRouter

router = APIRouter()


@router.get("/health/")
def is_health():
    return {
        "status":"ok",
        "service":"mini-ai-backend",
        "version":"0.1.0"
        }
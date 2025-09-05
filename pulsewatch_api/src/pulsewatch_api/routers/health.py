from fastapi import APIRouter

router = APIRouter()

@router.get("/live")
def live():
    return {"live": True}

@router.get("/ready")
def ready():
    return {"ready": True}

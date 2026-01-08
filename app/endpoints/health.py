from fastapi import APIRouter
from app.schemas.common import MessageResponse

router = APIRouter(
    prefix="/health",
    tags=["health"]
)


@router.get("/", response_model=MessageResponse)
def health_check():
    """
    Health check endpoint
    """
    return MessageResponse(message="OK")

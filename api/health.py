from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)

@router.get(
    "/health",
    summary="Health check del servicio",
    description="Verifica que la API esté levantada y operativa",
    response_model=dict,
)
def health():
    return {"status": "ok"}

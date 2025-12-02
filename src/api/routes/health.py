"""Health check routes for FKS Futures Service"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse({
        "status": "healthy",
        "service": "fks_futures",
        "timestamp": datetime.utcnow().isoformat()
    })

"""
FKS Futures Trading Service

This service provides:
- Futures market analysis (CME Group futures contracts)
- Signal generation for futures trading
- Integration with fks-app, fks-execution, and fks-data
"""
import logging
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Import routes
try:
    from api.routes.health import router as health_router
except ImportError:
    logger.warning("Could not import health router")
    health_router = None

app = FastAPI(
    title="FKS Futures Trading Service",
    description="Futures market analysis and signal generation for CME Group futures contracts",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
if health_router:
    app.include_router(health_router, tags=["health"])


@app.on_event("startup")
async def startup_event():
    """Initialize service on startup"""
    logger.info("Starting FKS Futures Trading Service...")
    logger.info("FKS Futures Trading Service started successfully")


@app.get("/")
async def root():
    """Root endpoint"""
    return JSONResponse({
        "service": "fks_futures",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "health": "/health"
        },
        "features": [
            "Futures market analysis",
            "Signal generation",
            "Integration with fks-app, fks-execution, fks-data"
        ]
    })


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("SERVICE_PORT", "8015"))
    uvicorn.run(app, host="0.0.0.0", port=port)

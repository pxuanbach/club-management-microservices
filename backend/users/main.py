from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from api import router as api_router
from event_handler import router as event_router


app = FastAPI(
    title="Users API",
    description="Under development",
    version="1.0",
    default_response_class=ORJSONResponse
)


@app.get("/")
async def root():
    """Health check."""
    # return {"detail": "Healthy!"}
    return ORJSONResponse(
        content={"detail": "Healthy!"}
    )


app.include_router(api_router)
app.include_router(event_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    expose_headers=["Content-Range", "Range"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=int("8001"),
    )
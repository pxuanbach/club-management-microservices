from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from routers import router


app = FastAPI(
    title="API Gateway",
    description="Development",
    version="1.0",
    default_response_class=ORJSONResponse
)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=int("8000"),
    )

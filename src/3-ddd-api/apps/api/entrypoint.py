from fastapi import FastAPI
from fastapi.responses import JSONResponse

from apps.api import context
from apps.api.config import configure_logging
from apps.api.domain.exceptions import DomainException
from apps.api.routes import people, default

configure_logging()

app = FastAPI(title="Training API", description="API for training", version="1.0.0")
context.Context()

app.include_router(default.router)
app.include_router(people.router)


@app.exception_handler(DomainException)
def handle_invalid_usage(response, error):
    return JSONResponse(error.to_dict(), status_code=error.status_code)
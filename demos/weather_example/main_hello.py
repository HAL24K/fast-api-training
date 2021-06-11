import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/')
def index():
    return {
        "message": "Hello world!",
        "status": "OK"
    }


uvicorn.run(api)

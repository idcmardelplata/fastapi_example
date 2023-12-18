from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware 

def configure_server(app):
    allowed_origins = [
       "http://localhost",
       "https://localhost",
       "http://localhost:8080",
        "https://localhost:443"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"]
        )
    app.add_middleware(GZipMiddleware, minimum_size=1000)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn
import logging
from router import users, posts, comments

HOST="0.0.0.0"
PORT=8080

allowed_origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
    "https://localhost:443",
]

app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"]
        )

app.add_middleware(GZipMiddleware, minimum_size=1000)


app.include_router(users)
app.include_router(posts)
app.include_router(comments)
    

if __name__ == "__main__":
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.WARNING, filename="logs/log", filemode="w+")

    try:
        config = uvicorn.Config(f"server:app", host=HOST, port=PORT, log_level="info", reload=True)
        server = uvicorn.Server(config)
        server.run()
        logging.log(msg="server as started sucefully", level=logging.INFO)

    except Exception as err:
        logging.error(msg=f"Failed to starting server: {err} ")

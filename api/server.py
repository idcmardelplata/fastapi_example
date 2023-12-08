from fastapi import FastAPI
import uvicorn
import logging
from router import users, posts, comments

app = FastAPI()

app.include_router(users)
app.include_router(posts)
app.include_router(comments)
    
config = uvicorn.Config(f"server:app", port="8080", log_level="info", reload=True)
server = uvicorn.Server(config)

if __name__ == "__main__":
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.WARNING, filename="logs/log", filemode="w+")
    try:
        server.run()
        logging.log("server as started sucefully")
    except Exception as err:
        logging.error("Failed to starting server: ", err)

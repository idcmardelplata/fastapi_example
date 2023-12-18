from fastapi import FastAPI
from api.configure_server import configure_server
import uvicorn
import logging
from router import user_route

HOST="0.0.0.0"
PORT=8080


app = FastAPI()
configure_server(app)

app.include_router(user_route)

if __name__ == "__main__":
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.WARNING, filename="logs/log", filemode="w+")

    try:
        config = uvicorn.Config(f"server:app", host=HOST, port=PORT, log_level="info", reload=True)
        server = uvicorn.Server(config)
        server.run()
        logging.log(msg="server as started sucefully", level=logging.INFO)

    except Exception as err:
        logging.error(msg=f"Failed to starting server: {err} ")

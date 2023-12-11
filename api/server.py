#HACK: 
""" 
Estas importaciones pueden moverse dentro del fichero 
__init__.py de la carpeta api, de esta manera queda mas
limpio y pueden llamarse asi:

import FastAPI, CORSMiddleware, GZipMiddleware, uvicorn, logging

IMPORTANTE: incluir en el __init__.py unicamente las llamadas
de las librerias pero no las llamadas a los modulos creados por vos (router en este caso).
Esto es asi porque cuando estas leyendo codigo la cantidad de imports ensucian la legibilidad
y de echo lo unico que puede llegar a interesarte es desde donde estas importando el resto de 
los componentes del sistema (que son los que vos creaste) :)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn
import logging

from router import users, posts, comments


#HACK:
"""
Todo este apartado de host, puerto, origenes permitidos y compresion en las peticiones
no son mas que temas de configuracion. Se podria crear un modulo de configuracion que lea
esos valores desde un fichero (yml, json  o toml) y los cargue automaticamente desde ahi.
Esto permite tener un codigo mas facil de cambiar y mantener, ademas de mucho mas legible.

La idea detras de esto es que sea sencillo cambiar las configuraciones cuando haya que hacer
un deploy, sino cuando haya que subir estos cambios al servidor vamos a tener que modificar el codigo
para simplemente poder cambiar el puerto, el host y los origenes permitidos ;)

Siempre en todo lo que es backend es necesario que estos valores sean leidos de forma
dinamica y que no esten hardcodeados.
"""
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

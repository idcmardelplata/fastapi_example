# There should be a way to optimize this file
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import APIRouter
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
from uuid import uuid4
from pydantic import BaseModel
from typing import Annotated
import uvicorn
import logging
import bcrypt

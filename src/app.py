from fastapi import FastAPI

import logging
from datetime import datetime

from src.util import read_yaml
from .db.users import models
from .db.database import engine
from .api.users import users

models.Base.metadata.create_all(bind=engine)

# Create Instance of FastAPI
app = FastAPI()

# Init Logger
logging.config.dictConfig(read_yaml('conf/log_config.yaml'))
logger_uvicorn = logging.getLogger("uvicorn")
logger_api = logging.getLogger('api')
logger_api.info(f'Log on {datetime.now()}')


app.include_router(users.router, prefix="/api")

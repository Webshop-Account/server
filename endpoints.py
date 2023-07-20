import logging
from logging.config import dictConfig

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from my_logger import LogConfig


dictConfig(LogConfig().model_dump())
logger = logging.getLogger("mylogger")

origins = ["*"]

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    # webbrowser.open("http://localhost:8080/statics")
    uvicorn.run(app, host="127.0.0.1", port=8080)

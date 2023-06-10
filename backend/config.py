import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB = os.getenv("POSTGRES_DB")
USERNAME = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")

__all__ = [DB, USERNAME, PASSWORD, HOST, PORT]
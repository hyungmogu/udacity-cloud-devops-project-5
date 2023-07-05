import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_MAX_REQUESTS_PER_DAY = os.getenv("API_MAX_REQUESTS_PER_DAY", 5)
API_SECONDS_IN_DAY = os.getenv("API_SECONDS_IN_DAY", 86400)

__all__ = ["API_MAX_REQUESTS_PER_DAY", "API_SECONDS_IN_DAY"]
from config import DB, USERNAME, PASSWORD, HOST, PORT
from sqlmodel import SQLModel, Session, create_engine

database_connection_url = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"
engine_url = create_engine(database_connection_url, echo=True)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session
from sqlmodel import SQLModel, Session, create_engine

database_connection_url = f"sqlite:////data/db/database.db"
engine_url = create_engine(database_connection_url, echo=True, connect_args={"check_same_thread": False})

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session
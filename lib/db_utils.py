from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///subtitles_vault_database.db"


class DatabaseManager:
    _instance = None

    def __new__(cls, database_url=DATABASE_URL):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._database_url = database_url
            cls._instance._engine = create_engine(database_url, echo=True)
            cls._instance._Session = sessionmaker(bind=cls._instance._engine)
            cls._instance._Base = declarative_base()
        return cls._instance

    def get_session(self):
        return self._Session()

    def get_engine(self):
        return self._engine

    def get_base(self):
        return self._Base

    def close_session(self):
        self._Session.close_all()

    def create_tables(self):
        self._Base.metadata.create_all(self._engine)


# Usage example:
if __name__ == "__main__":
    print("this is the db_utils module")

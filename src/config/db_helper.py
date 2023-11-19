from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from db_config import settings_db


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_engine(url, echo=echo)
        self.Session = sessionmaker(bind=self.engine)

    def get_scope_session(self):
        return scoped_session(self.Session)

    def get_db_session(self):
        session = self.Session()
        try:
            yield session
        except SQLAlchemyError:
            session.rollback()
            raise
        finally:
            session.close()

    def get_session(self):
        session = self.Session()
        try:
            yield session
        except SQLAlchemyError:
            session.rollback()
            raise
        finally:
            session.close()


db_helper = DatabaseHelper(settings_db.database_url, settings_db.DB_ECHO_LOG)

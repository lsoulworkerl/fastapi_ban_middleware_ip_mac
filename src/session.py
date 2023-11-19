from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config.db_config import settings_db


class SyncDatabaseSession:
    def __init__(self):
        self._engine = create_engine(
            settings_db.database_url,
            echo=settings_db.DB_ECHO_LOG
        )
        self._Session = sessionmaker(bind=self._engine)
        self._scoped_session = scoped_session(self._Session)

    def get_db_session(self):
        session = self._Session()
        return session

    def get_session(self):
        session = self._scoped_session()
        return session


sync_db_session = SyncDatabaseSession()
